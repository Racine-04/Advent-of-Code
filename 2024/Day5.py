import requests
import time

def isRightOrder(nums, order):
    printed = []
    for num in nums:
        befores = order.get(num, [])
        for before in befores:
            if before in printed:
                return False
        printed.append(num)
    return True

def order_list(nums, order):
    printed = []
    for num in nums:
        minimum = 100000000000
        befores = order.get(num, [])
        for before in befores:
            if before in printed:
                # get the smallest index and put if before
                minimum = min(minimum, printed.index(before))
        
        if minimum == 100000000000:
            printed.append(num)
        else:
            printed.insert(minimum, num)
    return printed


cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '5'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

isFirstPart = True
order = {}

sumPart1 = 0
sumPart2 = 0

for line in raw_puzzle_input.splitlines():
    if(line == ''):
        isFirstPart = False
        continue
    
    if isFirstPart:
        value = line.split("|")
        empty = []
        before = order.get(value[0], empty)
        order[value[0]] = before + [value[1]]
    else:
        nums = line.split(",")
        if isRightOrder(nums, order):
            sumPart1 += int(nums[len(nums)//2])
        else:
            ordered = order_list(nums, order)
            sumPart2 += int(ordered[len(ordered)//2])

print(sumPart1)
print(sumPart2)