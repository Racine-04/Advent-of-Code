import requests

def getAntinodePosition(antenna_one, antenna_two):
    if antenna_one == antenna_two:
        return (-1, -1)
    
    deltaX= 2*antenna_one[0] - antenna_two[0]
    deltaY= 2*antenna_one[1] - antenna_two[1]

    return (deltaX, deltaY)

def getVector(antenna_one, antenna_two):
    x = antenna_one[0] - antenna_two[0]
    y = antenna_one[1] - antenna_two[1]

    return (x, y)


cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '8'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text
locations = {}

matrix = []
i = 0

for line in raw_puzzle_input.splitlines():
    chars = list(line)
    for j in range(len(chars)):
        if chars[j] != '.':
            empty = []
            value = locations.get(chars[j], empty)
            locations[chars[j]] = value + [(i, j)]
    i += 1
    matrix.append(chars)

for antenna in locations.keys():
    postions = locations[antenna]
    if len(postions) == 1:
        continue

    for i in range(len(postions)):
        for j in range(len(postions)):
            antinodePostion = getAntinodePosition(postions[i], postions[j])
            vector = getVector(postions[i], postions[j])

            if(antinodePostion == (-1, -1)):
                matrix[postions[i][0]][postions[i][1]] = "#"

            # if(0<=antinodePostion[0]<len(matrix) and 0<= antinodePostion[1] < len(matrix[1])):
            while(0<=antinodePostion[0]<len(matrix) and 0<= antinodePostion[1] < len(matrix[1])):
                matrix[antinodePostion[0]][antinodePostion[1]] = "#"
                antinodePostion = (antinodePostion[0]+vector[0], antinodePostion[1]+vector[1])

time = 0
for line in matrix:
    time += line.count("#")

print(time)