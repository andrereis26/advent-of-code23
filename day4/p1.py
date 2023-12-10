file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()

sum = 0
for card in content.split("\n"):
    
    lWinNum = card.split("|")[0].strip().split()
    lMyNum = card.split("|")[1].strip().split()

    match = -1
    for i in range(len(lWinNum)):
        for j in range(len(lMyNum)):
            if lWinNum[i] == lMyNum[j]:
                match += 1
                
    sum += 2 ** match if match > -1 else 0
        
print(sum)