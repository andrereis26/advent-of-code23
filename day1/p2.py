
file_path = "./input.txt"

numsDic = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open(file_path, "r") as file:
    content = file.read()

sum = 0

for row in content.split("\n"):
    num=''
    c=0
    for char in row:
        if char.isdigit():
            num+=char
        else:
            for key in numsDic.keys():
                if key == row[c:c+len(key)]: 
                    num+=str(numsDic[key])
                    break
        c+=1
 
    
    sum += int(num[0]+ num[-1])
    
print(sum)
    



        