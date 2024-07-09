import random

def roll():
    die_roll = random.randint(1,6)
    return die_roll

while True:
    players = input("Enter the numbers of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2>= players <=4:
            break
        else:
            print("Enter the valid number of players.")
    else:
        print("Invalid input!")

max_score = 50
players_score = [0 for _ in range(players) ]

while max(players_score)< max_score:
    for each in range(players):
        print("\nPlayer number", each+1, "Start!")
        print("Your total score is", players_score[each])
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll the dice?")
            if should_roll.lower() !='y':
                break
            
            play = roll()
            if play == 1:
                print("You rolled the die and got 1! your score is set to 0.")
                print("Your turn is done!")
                current_score = 0
            else:
                print("You rolled the dice and got", play)
                current_score += play
            print("Youe score is", current_score)
        players_score[each] += current_score
        print("Your total score is", players_score[each]) 

highest_score = max[players_score]
winning_player = players_score.index(highest_score)
print("Player number", winning_player+1, "is the winner of the game with score", highest_score)