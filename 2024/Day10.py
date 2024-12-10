import requests

topographicMap = []

def getScore(position):
    stack = []
    score = 0

    stack.append(position)
    
    while(len(stack) > 0):
        location = stack.pop()
        currentValue = int(topographicMap[location[0]][location[1]])
        if(currentValue == 9):
            score += 1
        else:
            # try adding top
            if( 0 <= location[0] - 1 < len(topographicMap)):
                topValue = int(topographicMap[location[0]-1][location[1]])
                if (topValue == currentValue + 1):
                    stack.append((location[0] - 1,location[1]))

            # try adding Bottom
            if( 0 <= location[0] + 1 < len(topographicMap)):
                bottomValue = int(topographicMap[location[0]+1][location[1]])
                if (bottomValue == currentValue + 1):
                    stack.append((location[0]+1,location[1]))
            
            # try adding right
            if( 0 <= location[1] + 1 < len(topographicMap[0])):
                rightValue = int(topographicMap[location[0]][location[1] + 1])
                if (rightValue == currentValue + 1):
                    stack.append((location[0],location[1]+1))

            # try adding left
            if( 0 <= location[1] - 1 < len(topographicMap[0])):
                leftValue = int(topographicMap[location[0]][location[1] - 1])
                if (leftValue == currentValue + 1):
                    stack.append((location[0],location[1] - 1))

    return score


cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '10'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

zeroPositions = []

row = 0
for line in raw_puzzle_input.splitlines():
    numList = []
    for j in range(len(line)):
        if(line[j] == '0'):
            zeroPositions.append((row, j))
        numList.append(line[j])
    
    topographicMap.append(numList)
    row += 1

sum = 0
for position in zeroPositions:
    sum += getScore(position)

print(sum)