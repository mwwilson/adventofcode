f = open("day2input.txt", "r")
filestring = f.readlines()

def decryptHand(hand):
    if hand == "A" or hand == "X":
        return 0 #rock
    if hand == "B" or hand == "Y":
        return 1 #paper
    if hand == "C" or hand == "Z":
        return 2 #scissors

def scoreHand(player, opponent):
    if player == opponent:
        return 3 + player + 1
    if (player - opponent) % 3 == 2: # rock over paper, paper over scissors, scissors over paper
        return 0 + player + 1
    if (player - opponent) % 3 == 1:
        return 6 + player + 1

def scoreHandPart2(result, opponent):
    score = 0
    if result == 0: # scissors + lose means throw paper
        score = (opponent - 1) % 3 + 1 # 2
    if result == 2: # scissors + win means throw rock
        score = (opponent + 1) % 3 + 1 # 1
    if result == 1: # any + tie means throw the same
        score = opponent + 1
    
    return score + result * 3

score = 0
for match in filestring:
    hands = match.split()
    opponent = decryptHand(hands[0])
    player = decryptHand(hands[1])
    score = score + scoreHandPart2(player, opponent)

print(score)