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

def is_there_obstacle(position, direction, labyrinth):
    i = 1
    if direction == '^':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]-i][position[1]] == '#':
                return (True, (position[0]-i+1, position[1]))
            i += 1
        return (False, (position[0]-i+1, position[1]))
    elif direction == '<':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]][position[1]-i] == '#':
                return (True, (position[0], position[1]-i+1))
            i += 1
        return (False, (position[0], position[1]-i+1))
    elif direction == 'v':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]+i][position[1]] == '#':
                return (True, (position[0]+i-1, position[1]))
            i += 1
        return (False, (position[0]+i-1, position[1]))
    else:
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]][position[1]+i] == '#':
                return (True, (position[0], position[1]+i-1))
            i += 1
        return (False, (position[0], position[1]+i-1))

def is_back_to_intial(position, direction, labyrinth, initial):
    i = 1
    if direction == '^':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]-i][position[1]] == '#':
                return False
            elif position[0] - i == initial[0] and position[1] == initial[1]:
                return True
            i += 1
        return False
    elif direction == '<':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]][position[1]-i] == '#':
                return False
            elif position[0] == initial[0] and position[1]-i == initial[1]:
                return True
            i += 1
        return False
    elif direction == 'v':
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]+i][position[1]] == '#':
                return False
            elif position[0] + i == initial[0] and position[1] == initial[1]:
                return True
            i += 1
        return False
    else:
        while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
            if labyrinth[position[0]][position[1]+i] == '#':
                return False
            elif position[0] == initial[0] and position[1] + i == initial[1]:
                return True
            i += 1
        return False

def is_rectangle_possible(position, direction, labyrinth):
    initial = position
    value = []
    while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
        try:
            value = is_there_obstacle(position, direction, labyrinth)
            position = value[1]
            direction = rotate(direction)
            if(value[0]):
                if(is_back_to_intial(position, direction, labyrinth, initial) and is_there_obstacle(position, direction, labyrinth)[0]):
                    return True
        except:
            break
    
    return False

cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '6'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

direction = '^'
visited = {1}
obstacles = {1}
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
        chars.append(char)
        colone += 1
    labyrinth.append(chars)
    row +=1

infiniteLoop = 0

while 0 <= position[0] < len(labyrinth) and 0 <= position[1] < len(labyrinth[0]):
    try:
        if(is_rectangle_possible(position, direction, labyrinth) or is_rectangle_possible(position, rotate(direction), labyrinth)):
            print("here")
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
# print(obstacles)
print(len(obstacles)-1)