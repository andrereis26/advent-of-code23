file_path = "./input.txt"

with open(file_path, "r") as file:
    content = file.read()

cards=[]
matchers=[]
index = 0

for card in content.split("\n"):
    cards.append(1)

    lWinNum = card.split("|")[0].strip().split()
    lMyNum = card.split("|")[1].strip().split()

    match = 0
    for i in range(len(lWinNum)):
        for j in range(len(lMyNum)):
            if lWinNum[i] == lMyNum[j]:
                match += 1

    matchers.append(match)

for i in range(len(cards)):
    for j in range(matchers[i]):
        cards[i+j+1] += cards[i]
        
print(sum(cards))