import math
import random

dice = [
    random.randint(1,6),
    random.randint(1,6),
    random.randint(1,6),
    random.randint(1,6),
    random.randint(1,6)
]

held_dice = [
    0,
    0,
    0,
    0,
    0
]


holds = [
    False,
    False,
    False,
    False,
    False
    ]

scores = {
    "ones": -1, 
    "twos": -1, 
    "threes": -1, 
    "fours": -1, 
    "fives": -1, 
    "sixes": -1, 
    "three_of_kind": -1, 
    "four_of_kind": -1, 
    "full_house": -1, 
    "small_straight": -1, 
    "large_straight": -1, 
    "yahtzee": -1, 
    "chance": -1, 
    "upper_bonus": 0,
    "yahtzee_bonus": 0
}

hold_iterator = 0

def roll(held_dice, dice):
    for x in range(len(held_dice)):
        held_dice[x] = dice[x]

def holdit(held_dice,hold_iterator):
    print(" ")
    print(held_dice[0], held_dice[1], held_dice[2], held_dice[3], held_dice[4])
    print("__________")
    for x in range(0,5):
        choice = input("Die " + str(x+1) + ": hold the " +  str(held_dice[x]) + "? (y/n): ")
        if choice == "y":
            holds[x] = True
        elif choice == "n":
            holds[x] = False
        else:
            print("invalid choice: dice will be held")
            holds[x] = True

    for y in range(0,5):   
        if(holds[y] == False):
            held_dice[y] = random.randint(1,6)

def scoring(scores, held_dice):
    z = 1
    temp_score = 0
    
    for x, y in scores.items():
    
        if y == -1:
            print(z, " " + x + "___")
            z+=1
        else:
            print(z, " " + x, y)
            z+=1
    z = 1
    choice = int(input("Choose where to score: "))

    if choice == 1 and scores.get("ones") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 1:
                temp_score+=1
        scores.update({"ones": temp_score})
    elif choice == 2 and scores.get("twos") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 2:
                temp_score+=2
        scores.update({"twos": temp_score})
    elif choice == 3 and scores.get("threes") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 3:
                temp_score+=3
        scores.update({"threes": temp_score})
    elif choice == 4 and scores.get("fours") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 4:
                temp_score+=4
        scores.update({"fours": temp_score})
    elif choice == 5 and scores.get("fives") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 5:
                temp_score+=5
        scores.update({"fives": temp_score})
    elif choice == 6 and scores.get("sixes") == -1:
        for x in range(len(held_dice)):
            if held_dice[x] == 6:
                temp_score+=6
        scores.update({"sixes": temp_score})
    elif choice == 7 and scores.get("three_of_kind") == -1:
        for x in range(1, 7):
            if held_dice.count(x) >= 3:
                scores.update({"three_of_kind": sum(held_dice)}) 
            elif scores.get("three_of_kind") == -1:
                scores.update({"three_of_kind": 0})
    elif choice == 8 and scores.get("four_of_kind") == -1:
        for x in range(1,7):
            if held_dice.count(x) >= 4:
                scores.update({"four_of_kind": sum(held_dice)}) 
            elif scores.get("four_of_kind") == -1:
                scores.update({"four_of_kind": 0})
    elif choice == 9 and scores.get("full_house") == -1:
        check_2 = False
        check_3 = False
        for x in range(1,7):
            if held_dice.count(x) == 2:
                check_2 = True
            elif held_dice.count(x) == 3:
                check_3 = True
        if check_2 and check_3:
            scores.update({"full_house": 25})
        else:
            scores.update({"full_house": 0})
    elif choice == 10 and scores.get("small_straight") == -1:
        one = False
        two = False
        three = False
        four = False
        five = False
        six = False
        for x in range(len(held_dice)):
            if held_dice[x] == 1:
                one = True
            elif held_dice[x] == 2:
                two = True
            elif held_dice[x] == 3:
                three = True
            elif held_dice[x] == 4:
                four = True
            elif held_dice[x] == 5:
                five = True
            elif held_dice[x] == 6:
                six = True
        if (one and two and three and four) or (two and three and four and five) or (three and four and five and six):
            scores.update({"small_straight": 30})
        else:
            scores.update({"small_straight": 0})
    elif choice == 11 and scores.get("large_straight") == -1:
        one = False
        two = False
        three = False
        four = False
        five = False
        six = False
        for x in range(len(held_dice)):
            if held_dice[x] == 1:
                one = True
            elif held_dice[x] == 2:
                two = True
            elif held_dice[x] == 3:
                three = True
            elif held_dice[x] == 4:
                four = True
            elif held_dice[x] == 5:
                five = True
            elif held_dice[x] == 6:
                six = True
        if (one and two and three and four and five) or (two and three and four and five and six):
            scores.update({"large_straight": 40})
        else:
            scores.update({"large_straight": 0})
    elif choice == 12 and scores.get("yahtzee") == -1:
        for x in range(1, 7):
            if held_dice.count(x+1) >= 5 :
                scores.update({"yahtzee": 50}) 
            elif scores.get("yahtzee") == -1:
                scores.update({"yahtzee": 0})
    elif choice == 12 and scores.get("yahtzee") == 50 and scores.get("yahtzee_bonus") == 0:
        for x in range(1, 7):
            if held_dice.count(x+1) >= 5 :
                scores.update({"yahtzee_bonus": 100}) 
            else:
                scores.update({"yahtzee_bonus": 0})               
    elif choice == 13 and scores.get("chance") == -1:
        scores.update({"chance" : sum(held_dice)})
    else:
        print("invalid selection")
        return False
    
    bonus_check = scores.get("ones") + scores.get("twos") + scores.get("threes") + scores.get("fours") + scores.get("fives") + scores.get("sixes")
    print("bonus check", bonus_check)
    if bonus_check >= 63:
        scores.update({"upper_bonus" : 35}) 
            
    for x, y in scores.items():
    
        if y == -1:
            print(z, " " + x + "___")
            z+=1
        else:
            print(z, " " + x, y)
            z+=1
    
    return True


finish_test = False
while finish_test==False:   
    final_score_test = 0
    for x, val in scores.items():
        if int(val) <= -1:
            final_score_test+=1
    if final_score_test == 0:
        break

    print()
    roll(held_dice, dice)
    while hold_iterator < 2:
        holdit(held_dice,hold_iterator)
        if holds[0] == True and holds[1] == True and holds[2] == True and holds[3] == True and holds[4] == True:
            hold_iterator = 2
        hold_iterator+=1 


    print(" ")
    print(held_dice[0], held_dice[1], held_dice[2], held_dice[3], held_dice[4])
    print("__________")
    

    score_test = False
    while score_test == False:
        score_test = scoring(scores,held_dice)
        hold_iterator = 0
        for items in holds:
            holds[items] = False
        dice = [
        random.randint(1,6),
        random.randint(1,6),
        random.randint(1,6),
        random.randint(1,6),
        random.randint(1,6)
        ]

score = sum(scores.values())
print("Final Score =", score)

        






        


    
    
        












