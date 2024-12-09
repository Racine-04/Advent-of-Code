import requests

first = ()
obstacles = {1}

def rotate(direction):
    if direction == '^':
        return '>'
    elif direction == '<':
        return '^'
    elif direction == '>':
        return 'v'
    else:
        return '<'

def is_able_to_move(position, direction, labyrinth):
    if direction == '^':
        return labyrinth[position[0]-1][position[1]] != '#'
    elif direction == '<':
        return labyrinth[position[0]][position[1]-1] != '#'
    elif direction == 'v':
        return labyrinth[position[0]+1][position[1]] != '#'
    else:
        return labyrinth[position[0]][position[1]+1] != '#'

def move(position, direction):
    if direction == '^':
        return (position[0]-1, position[1])
    elif direction == '<':
        return (position[0],position[1]-1)
    elif direction == 'v':
        return (position[0]+1, position[1])
    else:
        return (position[0], position[1]+1)

def isObstruction(labyrinth, obstaclePositionsRow, obstaclePositionsColone, position, direction):
    cycle = {first}
    obstaclePosition = ()
    #Add new obstacle
    try:
        if direction == '^':
            newRow = position[0] - 1
            if(0 <= newRow < len(labyrinth) and labyrinth[newRow][position[1]] == "."):
                value = obstaclePositionsRow.get(newRow, [])
                obstaclePositionsRow[newRow] = value + [position[1]]

                value = obstaclePositionsColone.get(position[1], [])
                obstaclePositionsColone[position[1]] = value + [newRow]
                    
                obstaclePosition = (newRow, position[1])
        elif direction == '<':
            newColone = position[1] - 1
            if(0 <= newColone < len(labyrinth[0]) and labyrinth[position[0]][newColone] == "."):
                value = obstaclePositionsRow.get(position[0], [])
                obstaclePositionsRow[position[0]] = value + [newColone]

                value = obstaclePositionsColone.get(newColone, [])
                obstaclePositionsColone[newColone] = value + [position[0]]
                
                obstaclePosition = (position[0], newColone)
        elif direction == '>':
            newColone = position[1] + 1
            if(0 <= newColone < len(labyrinth[0]) and labyrinth[position[0]][newColone] == "."):
                value = obstaclePositionsRow.get(position[0], [])
                obstaclePositionsRow[position[0]] = value + [newColone]

                value = obstaclePositionsColone.get(newColone, [])
                obstaclePositionsColone[newColone] = value + [position[0]]

                obstaclePosition = (position[0], newColone)
        else:
            newRow = position[0] + 1
            if(0 <= newRow < len(labyrinth) and labyrinth[newRow][position[1]] == "."):
                value = obstaclePositionsRow.get(newRow, [])
                obstaclePositionsRow[newRow] = value + [position[1]]

                value = obstaclePositionsColone.get(position[1], [])
                obstaclePositionsColone[position[1]] = value + [newRow]
                obstaclePosition = (newRow, position[1])
    except:
        pass
    
    position = first[0]
    direction = first[1]
    while 0 <= position[0] < (len(labyrinth) - 1) and 0 <= position[1] < (len(labyrinth[0]) - 1):
        if direction == '^':
            rowObstacles = obstaclePositionsColone.get(position[1], [])
            distance = -1000000
            for rowObstacle in rowObstacles:
                if(rowObstacle - position[0] < 0):
                    distance = max(distance, rowObstacle - position[0])
            
            position = (position[0] + distance + 1, position[1])

        elif direction == '<':
            coloneObstacles = obstaclePositionsRow.get(position[0], [])
            distance = -1000000
            for coloneObstacle in coloneObstacles:
                if(coloneObstacle - position[1] < 0):
                    distance = max(distance, coloneObstacle - position[1])
            
            position = (position[0], position[1] + distance + 1)
        elif direction == '>':
            coloneObstacles = obstaclePositionsRow.get(position[0], [])
            distance = 1000000
            for coloneObstacle in coloneObstacles:
                if(coloneObstacle - position[1] > 0):
                    distance = min(distance, coloneObstacle - position[1])
            
            position = (position[0], position[1] + distance - 1)

        else:
            rowObstacles = obstaclePositionsColone.get(position[1], [])
            distance = 1000000
            for rowObstacle in rowObstacles:
                if(rowObstacle - position[0] > 0):
                    distance = min(distance, rowObstacle - position[0])
            
            position = (position[0] + distance - 1, position[1])

        direction = rotate(direction)
        status = ((position, direction))

        if(status in cycle):
            obstacles.add(obstaclePosition)
            break

        cycle.add(status)


cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '6'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input =  req.text

direction = '^'
visited = {1}
obstaclePositionsRow = {}
obstaclePositionsColone = {}
position = ()
labyrinth = []
row = 0
for line in raw_puzzle_input.splitlines():
    colone = 0
    chars = []
    for char in line:
        if char == '^' or char == '<' or char == 'v' or char == '>':
            direction = char
            position = (row, colone)
            first = (position, direction)
            visited.add(position)
        elif char == '#':
            value = obstaclePositionsRow.get(row, [])
            obstaclePositionsRow[row] = value + [colone]

            value = obstaclePositionsColone.get(colone, [])
            obstaclePositionsColone[colone] = value + [row]

        chars.append(char)
        colone += 1
    labyrinth.append(chars)
    row +=1

infiniteLoop = 0

while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
    try:

        isObstruction(labyrinth, obstaclePositionsRow.copy(), obstaclePositionsColone.copy(), position, direction)

        if(is_able_to_move(position, direction, labyrinth)):
            position = move(position, direction)
            if( 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0])):
                visited.add(position)
        else:
            direction = rotate(direction)
    except Exception as e:
        break

print(len(visited)-1)
print(len(obstacles)-1)