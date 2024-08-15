

name = input("Enter your name:")
print("Hello. Welcome to this adventure game,", name, ".")
print("Lets start the game!")

choice = input("You are on top of a hill. You slowly walk downhill and then come across an intersection. Choose where to go(left/right).").lower()
if choice == 'left':
    choice = input("You take the road on the left and then come across a small hut. Do you open the door to explore the hut or continue to your own way. Type open to explore or continue to not.")
    if choice == 'open':
        print("You open the door to the hut. You start going room to room when all of a sudden an angry witch hits you from the back and you die.")
        print("You lost the game.")
    elif choice== 'continue':
        print("After a few steps you are met with a dead end. You lose the game.")
    else:
        print("Not a valid option. You lose")
elif choice =='right':                                       
    choice = input("You see a man walking opposite you. He starts to wave at you. Type talk to strike a conversation or continue to go on your own way.")
    if choice == 'talk':
        print("You have a good conversation with the man. He is happy to have someone to talk to after so long. so he gives you a bag of gold. You win!")
    elif choice =='continue':
        print("The man is offended that you ignored him so he turns you into a stone. You lose")
    else:
        print("Not a valid option. You lose")
print("Thankyou for trying the game!")