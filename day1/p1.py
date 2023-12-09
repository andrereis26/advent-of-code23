
file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()

sum = 0

for row in content.split("\n"):
    num=''
    for char in row:
        if char.isdigit():
            num+=char
 
    
    sum += int(num[0]+ num[-1])
    
print(sum)
    



        