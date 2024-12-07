import requests
import re

def mul(x, y):
    return x*y

cookies = {}
cookies['session'] = '53616c7465645f5fd289b22cc7e55adb9976b44c511ae63ba61eb120770a16fd739005f66f774400f572b7bc95a57a10f7e96ad761262822136398cbe5f897f1'

puzzle_year = '2024'
puzzle_day = '3'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = "do()" + req.text.replace('\n', ' ')

match = re.findall("do\(\)(?:(?!don't).)*", raw_puzzle_input)

stringMatch = "".join(match)

clean_match = re.findall("mul[(][0-9]+,[0-9]+[)]", stringMatch)

sum = 0
for line in clean_match:
    sum += eval(line)

print(sum)