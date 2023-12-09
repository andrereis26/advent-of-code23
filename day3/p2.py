def checkAdjacent(i, j, visited):
    mult = 1
    partNum=0
    
    def isValid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[i]) and (x, y) not in visited

    if isValid(i, j - 1) and matrix[i][j - 1].isdigit():  # left
        mult *= getFullNum(i, j - 1,visited)
        partNum += 1
        
    if isValid(i, j + 1) and matrix[i][j + 1].isdigit():  # right
        mult *= getFullNum(i, j + 1,visited)
        partNum += 1
        
    if isValid(i - 1, j) and matrix[i - 1][j].isdigit():  # top
        mult *= getFullNum(i - 1, j,visited)
        partNum += 1
        
    if isValid(i + 1, j) and matrix[i + 1][j].isdigit():  # bottom
        mult *= getFullNum(i + 1, j,visited)
        partNum += 1
        
    if isValid(i - 1, j - 1) and matrix[i - 1][j - 1].isdigit():  # top left
        mult *= getFullNum(i - 1, j - 1,visited)
        partNum += 1
        
    if isValid(i + 1, j + 1) and matrix[i + 1][j + 1].isdigit():  # bottom right
        mult *= getFullNum(i + 1, j + 1,visited)
        partNum += 1
        
    if isValid(i - 1, j + 1) and matrix[i - 1][j + 1].isdigit():  # top right
        mult *= getFullNum(i - 1, j + 1,visited)
        partNum += 1
        
    if isValid(i + 1, j - 1) and matrix[i + 1][j - 1].isdigit():  # bottom left
        mult *= getFullNum(i + 1, j - 1,visited)
        partNum += 1

    if partNum == 2:
        # print("found a gear: " + str(mult))
        return mult
    
    return 0



# gets the numbers at the rigt and left of the current number
def getFullNum(i,j, visited):
    num = matrix[i][j]
    visited.add((i, j))
    
    leftJ = j - 1
    while leftJ >= 0 and matrix[i][leftJ].isdigit(): # left
        num = matrix[i][leftJ] + num
        visited.add((i, leftJ))
        leftJ-=1
    
    rightJ = j + 1
    while rightJ < len(matrix[i]) and matrix[i][rightJ].isdigit():
        num = num + matrix[i][rightJ]
        visited.add((i, rightJ))
        rightJ+=1
    
    # print(num)
    return int(num)
    
    
    
file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()
    
tot = 0  
matrix = content.split("\n")
visited = set()

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == "*":
            tot+=checkAdjacent(i, j, visited)
            
print(tot)       

           
            
