
file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()


sum = 0

for game in content.split("\n"):
    
    id = game.split(":")[0].split()[1]    
    sets = game.split(":")[1].split(";")
    
    minRed=0
    minGreen=0
    minBlue=0

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
        
            if cubes["red"] > minRed:
                minRed = cubes["red"]
                
            if cubes["green"] > minGreen:
                minGreen = cubes["green"]
                
            if cubes["blue"] > minBlue:
                minBlue = cubes["blue"]
        
    
    sum+=minRed*minGreen*minBlue

print(sum)
    