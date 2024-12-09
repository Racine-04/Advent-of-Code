import requests

cookies = {}
cookies['session'] = '53616c7465645f5f2e0526ba5e5de2eb1dbe3689785a93e8555dc7247aa39344df8aad0931492841d4573b34bf54fbfaa35d99ef6af4d4a4ab5b54175694088e'

puzzle_year = '2024'
puzzle_day = '9'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
diskMap = list("2333133121414131402")

id = 0
idCount = {}
space = {}
rearrangedDiskMap = []
for i in range(len(diskMap)):
    if(diskMap[i] == '\n'):
        continue
    if(i % 2 == 0):
        for j in range(int(diskMap[i])):
            rearrangedDiskMap.append(str(id))
        idCount[id] = int(diskMap[i])
        id += 1
    else:
        for j in range(int(diskMap[i])):
            rearrangedDiskMap.append(".")
        
        space[id - 1] = int(diskMap[i])

left = 0
right = len(rearrangedDiskMap) - 1

while(left < right):
    if(rearrangedDiskMap[left] != "."):
        left += 1
    elif(rearrangedDiskMap[right] == "."):
        right -= 1
    else:
        rearrangedDiskMap[left], rearrangedDiskMap[right] = rearrangedDiskMap[right], rearrangedDiskMap[left]

i = 0
sum = 0
while i < len(rearrangedDiskMap):
    if(rearrangedDiskMap[i] != "."):
        sum += i * int(rearrangedDiskMap[i])
    i +=1

print(sum)