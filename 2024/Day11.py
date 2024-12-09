import requests

cookies = {}
cookies['session'] = '53616c7465645f5f2e0526ba5e5de2eb1dbe3689785a93e8555dc7247aa39344df8aad0931492841d4573b34bf54fbfaa35d99ef6af4d4a4ab5b54175694088e'

puzzle_year = '2024'
puzzle_day = '11'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = "2024"

nums = raw_puzzle_input.split(" ")

for i in range(25):
    newArray = []
    for num in nums:
        if(num == '0'):
            newArray.append('1')
        elif len(num) % 2 == 0:
            half = len(num) // 2
            newArray.append(str(int(num[:half])))
            newArray.append(str(int(num[half:])))
        else:
            newArray.append(str(int(num)*2024))
    nums = newArray

print(len(nums))