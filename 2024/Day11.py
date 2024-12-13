# import requests
tracker = {-1}

def blink(stringNum):
    newArray = []
    if(stringNum == '0'):
        num = '1'
        tracker.add(num)
        newArray.append(num)
    elif len(stringNum) % 2 == 0:
        half = len(stringNum) // 2
        num1 = str(int(stringNum[:half]))
        num2 = str(int(stringNum[:half]))
        tracker.add(num1)
        tracker.add(num2)
        newArray.append(num1)
        newArray.append(num2)
    else:
        num = str(int(stringNum)*2024)
        tracker.add(num)
        newArray.append(num)
    
    return newArray
    
cookies = {}
cookies['session'] = '53616c7465645f5f2e0526ba5e5de2eb1dbe3689785a93e8555dc7247aa39344df8aad0931492841d4573b34bf54fbfaa35d99ef6af4d4a4ab5b54175694088e'

puzzle_year = '2024'
puzzle_day = '11'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

# req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = "125 17"

nums = raw_puzzle_input.split(" ")

cache = {}
previousSize = 1

i = 75
while i > 0:
    temp = []
    
    # Get max count
    maximum = 1
    for key in cache.keys():
        if key in tracker:
            size = len(cache[key])
            if(size <= i):
                maximum = max(maximum, size)

    for num in nums:
        value = cache.get(num, blink(num))
        cache[num] = value
        while len(value) < maximum + 1:
            arr = []
            maxCalculated = value[len(value)-1]

            for numbers in maxCalculated:
                arr += blink(numbers)

            cache[num] += arr

        temp += cache[num][len(value)-1]
    nums = temp
    
    i -= maximum

print(len(nums))