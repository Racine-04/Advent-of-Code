import requests

cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '13'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

inputs = raw_puzzle_input.splitlines()

minimumToken = 0
for i in range(0, len(inputs), 4):
    buttonA = (int(inputs[i][12:14]), int(inputs[i][18:]))
    buttonB = (int(inputs[i + 1][12:14]), int(inputs[i + 1][18:]))

    xTarget = ""
    j = 9
    while inputs[i+2][j] != ",":
        xTarget += inputs[i+2][j]
        j +=1
    
    yTarget = ""    
    j += 4
    while j < len(inputs[i+2]):
        yTarget += inputs[i+2][j]
        j += 1

    target = (int(xTarget) + 10000000000000, int(yTarget) + 10000000000000)
    minimum = 100000000
    
    for a in range(10000000):
        for b in range(10000000):
            xSum = a * buttonA[0] + b * buttonB[0]
            ySum = a * buttonA[1] + b * buttonB[1]
            if (xSum == target[0] and ySum == target[1]):
                tokenSum = (a * 3) + b 
                minimum = min(minimum, tokenSum)
            elif (xSum > target[0] or ySum > target[1]):
                break
        
        if(a * buttonA[0] > target[0] or a * buttonA[1] > target[1] or a*3 >= minimum):
            break
    
    if (minimum != 100000000):
        minimumToken += minimum


print(minimumToken)  