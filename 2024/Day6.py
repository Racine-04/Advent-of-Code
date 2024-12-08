import requests

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
    initialPosition = position
    # initialDirection = direction
    
    if direction == '^':
            value = obstaclePositionsRow.get(position[0] - 1, [])
            obstaclePositionsRow[position[0] - 1] = value + [position[1]]

            value = obstaclePositionsColone.get(position[1], [])
            obstaclePositionsColone[position[1]] = value + [position[0] - 1]

    elif direction == '<':
            value = obstaclePositionsRow.get(position[0], [])
            obstaclePositionsRow[position[0]] = value + [position[1] - 1]

            value = obstaclePositionsColone.get(position[1] - 1, [])
            obstaclePositionsColone[position[1] - 1] = value + [position[0]]

    elif direction == '>':
            value = obstaclePositionsRow.get(position[0], [])
            obstaclePositionsRow[position[0]] = value + [position[1] + 1]

            value = obstaclePositionsColone.get(position[1] + 1, [])
            obstaclePositionsColone[position[1] + 1] = value + [position[0]]

    else:
            value = obstaclePositionsRow.get(position[0] + 1, [])
            obstaclePositionsRow[position[0] + 1] = value + [position[1]]

            value = obstaclePositionsColone.get(position[1], [])
            obstaclePositionsColone[position[1]] = value + [position[0] + 1]

    while 0 <= position[0] < (len(labyrinth) - 1) and 0 <= position[1] < (len(labyrinth[0]) - 1):
        if direction == '^':
            rowObstacles = obstaclePositionsColone[position[1]]
            distance = 1000000
            for rowObstacle in rowObstacles:
                if(distance < 0):
                    distance = min(distance, rowObstacle - position[0])
            
            position = (position[0] + distance + 1, position[1])

        elif direction == '<':
            coloneObstacles = obstaclePositionsRow[position[0]]
            distance = 1000000
            for coloneObstacle in coloneObstacles:
                if(distance < 0):
                    distance = min(distance, coloneObstacle - position[1])
            
            position = (position[0], position[1] + distance + 1)
        elif direction == '>':
            coloneObstacles = obstaclePositionsRow[position[0]]
            distance = 1000000
            for coloneObstacle in coloneObstacles:
                if(distance > 0):
                    distance = min(distance, coloneObstacle - position[1])
            
            position = (position[0], position[1] + distance - 1)

        else:
            rowObstacles = obstaclePositionsColone[position[1]]
            distance = 1000000
            for rowObstacle in rowObstacles:
                if(distance > 0):
                    distance = min(distance, rowObstacle - position[0])
            
            position = (position[0] + distance - 1, position[1])

        direction = rotate(direction)

        if(position == initialPosition):
            return True

    return False


cookies = {}
cookies['session'] = '53616c7465645f5f2e0526ba5e5de2eb1dbe3689785a93e8555dc7247aa39344df8aad0931492841d4573b34bf54fbfaa35d99ef6af4d4a4ab5b54175694088e'

puzzle_year = '2024'
puzzle_day = '6'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

direction = '^'
visited = {1}
obstacles = {1}
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
        if(isObstruction(labyrinth, obstaclePositionsRow.copy(), obstaclePositionsColone.copy(), position, direction)):
            obstacles.add(position)

        if(is_able_to_move(position, direction, labyrinth)):
            position = move(position, direction)
            if( 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0])):
                visited.add(position)
        else:
            direction = rotate(direction)
    except:
        break

print(len(visited)-1)
print(obstacles)
print(len(obstacles)-1)