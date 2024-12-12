import requests

garden = []

def getPrice(i, j):
    stack = [] 
    region = garden[i][j]

    if(region.islower()):
        return 0
    
    garden[i][j] = region.lower()

    stack.append((i, j))

    area = 0
    perimeter = 0
    while len(stack) > 0:
        position = stack.pop()

        # Up
        if(0 <= position[0] - 1 < len(garden)):
            if garden[position[0] - 1][position[1]] == region:
                garden[position[0] - 1][position[1]] = region.lower()
                stack.append((position[0] - 1, position[1]))
            else:
                if garden[position[0] - 1][position[1]] != region.lower():
                    perimeter += 1
        else:
            perimeter+=1

        # Down
        if(0 <= position[0] + 1 < len(garden)):
            if garden[position[0] + 1][position[1]] == region:
                garden[position[0] + 1][position[1]] = region.lower()
                stack.append((position[0] + 1, position[1]))
            else:
                if garden[position[0] + 1][position[1]] != region.lower():
                    perimeter += 1
        else:
            perimeter+=1

        # Left
        if(0 <= position[1] - 1 < len(garden[0])):
            if garden[position[0]][position[1] - 1] == region:
                garden[position[0]][position[1] - 1] = region.lower()
                stack.append((position[0], position[1] - 1))
            else:
                if garden[position[0]][position[1] - 1] != region.lower():
                    perimeter += 1
        else:
            perimeter+=1

        # Right
        if(0 <= position[1] + 1 < len(garden[0])):
            if garden[position[0]][position[1] + 1] == region:
                garden[position[0]][position[1] + 1] = region.lower()
                stack.append((position[0], position[1] + 1))
            else:
                if garden[position[0]][position[1] + 1] != region.lower():
                    perimeter += 1
        else:
            perimeter+=1
        
        area += 1
    return area * perimeter






cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '12'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

regions = {}

totalPrice = 0
for line in raw_puzzle_input.splitlines():
    garden.append(list(line))

for i in range(len(garden)):
    for j in range(len(garden[0])):

        totalPrice += getPrice(i, j)

print(totalPrice)