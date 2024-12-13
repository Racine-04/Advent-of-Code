import requests

garden = []
rowMap = {}
colMap = {}

def getNumSides(region):
    rowSides = 0

    for key in rowMap.keys():
        positions = rowMap[key]
        positions.sort()

        for i in range(len(positions)):
            if(garden[key][positions[i] - 1] != ):

    for i in range(len(garden)):
        isInRegion = False
        if(garden[i][0] == region):
            isInRegion = True
        for j in range(len(garden[0])):
            if(garden[i][j] == region and not isInRegion):
                isInRegion = True
                rowSides += 1
            elif(garden[i][j] != region and isInRegion):
                isInRegion = False
                rowSides += 1
    colSides = 2

    
    return rowSides + colSides
        
            
def addMap(i, j):
    rowValue = rowMap.get(i, [])
    rowMap[i] = rowValue + [j]
    
    colValue = rowMap.get(j, [])
    rowMap[j] = colValue + [i]

def getPrice(i, j):
    stack = []
    region = garden[i][j]
    
    rowMap.clear()
    colMap.clear()

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
                addMap(position[0] - 1, position[1])
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
                addMap(position[0] + 1, position[1])
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
                addMap(position[0], position[1] - 1)
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
                addMap(position[0], position[1] + 1)
            else:
                if garden[position[0]][position[1] + 1] != region.lower():
                    perimeter += 1
        else:
            perimeter+=1
        
        area += 1

    sides = getNumSides(region.lower())

    print(region, area, sides)
    return area * sides






cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '12'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = '''AAAA
BBCD
BBCC
EEEC'''

regions = {}

totalPrice = 0
for line in raw_puzzle_input.splitlines():
    garden.append(list(line))

for i in range(len(garden)):
    for j in range(len(garden[0])):

        totalPrice += getPrice(i, j)

print(totalPrice)