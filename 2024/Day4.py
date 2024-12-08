import requests

def xmasCount(matrix, x, y):
    count = 0

    #Try down
    try:
        if(matrix[x-1][y] == 'M' and matrix[x-2][y] == 'A' and matrix[x-3][y] == 'S' and x-3>=0):
            count +=1
    except:
        pass
    
    #Try up
    try:
        if(matrix[x+1][y] == 'M' and matrix[x+2][y] == 'A' and matrix[x+3][y] == 'S'):
            count +=1
    except:
        pass    
    
    #Try right
    try:
        if(matrix[x][y+1] == 'M' and matrix[x][y+2] == 'A' and matrix[x][y+3] == 'S'):
            count +=1
    except:
        pass

    #Try left
    try:
        if(matrix[x][y-1] == 'M' and matrix[x][y-2] == 'A' and matrix[x][y-3] == 'S' and y-3>=0):
            count +=1
    except:
        pass    

    #Try diag bottom right
    try:
        if(matrix[x-1][y+1] == 'M' and matrix[x-2][y+2] == 'A' and matrix[x-3][y+3] == 'S' and x-3>=0):
            count +=1
    except:
        pass
    
    #Try diag top right
    try:
        if(matrix[x+1][y+1] == 'M' and matrix[x+2][y+2] == 'A' and matrix[x+3][y+3] == 'S'):
            count +=1
    except:
        pass    
    
    #Try diag bottom left
    try:
        if(matrix[x-1][y-1] == 'M' and matrix[x-2][y-2] == 'A' and matrix[x-3][y-3] == 'S' and x-3>=0 and y-3>=0):
            count +=1
    except:
        pass

    #Try diag top left
    try:
        if(matrix[x+1][y-1] == 'M' and matrix[x+2][y-2] == 'A' and matrix[x+3][y-3] == 'S' and y-3>=0):
            count +=1
    except:
        pass  

    return count

def masCount(matrix, x, y):    
    count = 0
    # matrix[x+1][y+1] == matrix[x+1][y-1] and matrix[x+1][y-1] == matrix[x-1][y-1] and matrix[x+1][y+1]==matrix[x-1][y+1] and matrix[x-1][y-1]==matrix[x-1][y+1]
    try:
        if(matrix[x+1][y+1] == matrix[x+1][y-1] == 'S' and matrix[x-1][y-1]==matrix[x-1][y+1] == 'M' and x-1>=0 and y-1>=0):
            return 1
        elif matrix[x+1][y+1] == matrix[x+1][y-1] == 'M' and matrix[x-1][y-1]==matrix[x-1][y+1] == 'S' and x-1>=0 and y-1>=0:
            return 1
        elif matrix[x+1][y-1] == matrix[x-1][y-1] == 'S' and matrix[x+1][y+1]==matrix[x-1][y+1] == 'M' and x-1>=0 and y-1>=0:
            return 1
        elif matrix[x+1][y-1] == matrix[x-1][y-1] == 'M' and matrix[x+1][y+1]==matrix[x-1][y+1] == 'S' and x-1>=0 and y-1>=0:
            return 1
    except:
        pass

    return 0



cookies = {}
cookies['session'] = 'MINDYOURBUISNESS'

puzzle_year = '2024'
puzzle_day = '4'
puzzle_input_url = f'https://adventofcode.com/{puzzle_year}/day/{puzzle_day}/input'

req = requests.get(puzzle_input_url, cookies=cookies)
raw_puzzle_input = req.text

matrix = []
for line in raw_puzzle_input.splitlines():
    chars = []
    for char in line:
        chars.append(char)

    matrix.append(chars)

sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j] == 'A'):
            sum += masCount(matrix, i, j)

print(sum)