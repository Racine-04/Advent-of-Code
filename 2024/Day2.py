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
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

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