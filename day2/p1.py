
file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()

nRed=12
nGreen=13
nBlue=14
sum = 0

for game in content.split("\n"):
    
    id = game.split(":")[0].split()[1]    
    sets = game.split(":")[1].split(";")
    valid = True
    
    for s in sets:    
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0    
        }
        
        draws = s.split(",")
        
        for d in draws:
            
            bInfo = d.split()
            
            cubes[bInfo[1]] += int(bInfo[0])
        
        if cubes["red"] > nRed or cubes["green"] > nGreen or cubes["blue"] > nBlue:
            valid = False
            break
    
    if valid:
        sum += int(id)
            

print(sum)
    