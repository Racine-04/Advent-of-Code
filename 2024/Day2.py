def isSafe(x):
    isIncreasing = int(x[0]) < int(x[1])

    for i in range(len(x)-1):
        if isIncreasing:
            if(int(x[i+1]) >= int(x[i]) + 4 or int(x[i+1])<=int(x[i])):
                return False
        else:
            if(int(x[i+1]) <= int(x[i]) - 4 or int(x[i+1])>=int(x[i])):
                return False
    return True

import requests

cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '2'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

safe = 0

for line in raw_puzzle_input.splitlines():
    x = line.split()

    if isSafe(x):
        safe +=1
    else:
        j = 0
        for i in range(len(x)):
            partition = x.copy()
            partition.pop(i)

            if(isSafe(partition)):
                safe += 1
                break
            

print(safe)