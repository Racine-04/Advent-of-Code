import requests

cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '1'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text
list1 = []
list2 = []
count = {}

for line in raw_puzzle_input.splitlines():
    x = line.split()
    list1.append(int(x[0]))
    list2.append(int(x[1]))

# list1.sort()
# list2.sort()

sum = 0
for i in range(len(list2)):
    count[list2[i]] = count.get(list2[i], 0) + 1

for num in list1:
    sum += num * count.get(num, 0)

print(sum)