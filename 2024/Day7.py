import requests

def getBinaryArray(num, size):
    binary = []
    while(num!=0):
        binary.append(num % 2)
        num = num // 2

    while len(binary) != size:
        binary.append(0)

    binary.reverse()
    return binary

def getTernaryArray(num, size):
    ternary = []
    while(num!=0):
        ternary.append(num % 3)
        num = num // 3

    while len(ternary) != size:
        ternary.append(0)

    ternary.reverse()
    return ternary

def isBinaryCombinationPossible(target, numbers):
    target = int(target)
    combination = len(numbers) - 1

    if(len(numbers)==1):
        return numbers[0] == target

    for i in range(2 ** (len(numbers)-1)):
        binary = getBinaryArray(i, combination)
        previous = int(numbers[0])
        
        for j in range(1,len(numbers)):
            if(binary[j-1] == 0):
                previous += int(numbers[j])
            else:
                previous *= int(numbers[j])

        if(previous == target):
            return True

    return False

def isTernaryCombinationPossible(target, numbers):
    target = int(target)
    combination = len(numbers) - 1

    if(len(numbers)==1):
        return numbers[0] == target

    for i in range(3 ** (len(numbers)-1)):
        ternary = getTernaryArray(i, combination)
        previous = int(numbers[0])
        
        for j in range(1,len(numbers)):
            if(ternary[j-1] == 0):
                previous += int(numbers[j])
            elif(ternary[j-1] == 1):
                previous *= int(numbers[j])
            else:
                previous = int(str(previous)+numbers[j])
        
        if(previous == target):
            return True

    return False

cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '7'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

sum = 0
for line in raw_puzzle_input.splitlines():
    i = 0
    target = ''

    while line[i] != ':':
        target += line[i]
        i+=1

    subString = line[i+2:]
    numbers = subString.split(" ")

    if(isTernaryCombinationPossible(target, numbers)):
        sum += int(target)

print(sum)
