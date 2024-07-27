import random

user_wins = 0 
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Choose Rock/Paper/Scissor to play or Q to Quit. ").lower()
    if user_pick == 'q':
        break
    if user_pick not in options:
        print("Invalid choice! Please choose either rock, paper, or scissor.")
        continue
    random_num = random.randint(0,2)
    #0 = rock, 1 = paper, 2 = scissor
    computer_pick = options[random_num]
    print("The computer chose", computer_pick)

    if user_pick=='rock' and computer_pick =='scissor':
        print("You won!")
        user_wins += 1
    elif user_pick == computer_pick:
        print("Its a tie!")
        continue
    elif user_pick=='scissor' and computer_pick =='paper':
        print("You won!")
        user_wins +=1
    elif user_pick =='paper' and computer_pick =='rock':
        print("You won!")
        user_wins +=1
    else:
        print("You lost!")
        computer_wins +=1

print("You won", user_wins, "times")
print("You lost", computer_wins, "times")
if user_wins > computer_wins:
    print("Congratulations!! You win the overall game.")
elif user_wins== computer_wins:
    print("Nobody won. It's a tie. Try again to win.")
else:
    print("You lost in the overall match. Better luck next time!")
print("Goodbye")