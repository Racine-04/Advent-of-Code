import requests

cookies = {}
cookies['session'] = '53616c7465645f5f2e0526ba5e5de2eb1dbe3689785a93e8555dc7247aa39344df8aad0931492841d4573b34bf54fbfaa35d99ef6af4d4a4ab5b54175694088e'

puzzle_year = '2024'
puzzle_day = '9'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
diskMap = list(req.text)

id = 0
idCount = {}
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
        
left = 0
right = len(rearrangedDiskMap) - 1
moved = {-1}

while(left < right):
    if rearrangedDiskMap[right] == ".":
        right -= 1
    elif rearrangedDiskMap[right] not in moved: 
        groupSize = idCount[int(rearrangedDiskMap[right])]
        groupStartIndex = right - groupSize + 1
        
        i = 0
        space = 0
        start = 0
        while i < len(rearrangedDiskMap) and i < groupStartIndex:
            if rearrangedDiskMap[i] == ".":
                start = start or i
                space += 1
            else:
                if(groupSize <= space):
                    # Add
                    for j in range(groupSize):
                        rearrangedDiskMap[j + start] = rearrangedDiskMap[right]

                    # Remove
                    for j in range(groupSize):
                        rearrangedDiskMap[j+groupStartIndex] = "."
                    
                    break
                space = 0
                start = 0
            i += 1

        moved.add(rearrangedDiskMap[right])
        right = groupStartIndex - 1
    else:
        right -= 1

i = 0
sum = 0
while i < len(rearrangedDiskMap):
    if(rearrangedDiskMap[i] != "."):
        sum += i * int(rearrangedDiskMap[i])
    i +=1

print(sum)