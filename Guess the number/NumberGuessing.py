import random 
given_range = input("Enter the range for the number: ")
if given_range.isdigit():
    given_range = int(given_range)
    if given_range<=0:
        print("Please enter a number greater than 0 next time!")
        quit()
else:
    print ("Please enter a number next time!")
    quit()

random_num = random.randint(0, given_range)
guess_num = 0 
while True:
    print("Guess the Number!!")
    user_guess = input("Enter your guess: ")
    guess_num += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Enter a number next time.")
        continue
    if user_guess == random_num:
        print("You guessed correctly!")
        break
    elif user_guess> random_num:
        print("Your guess is greater.")
    else:
        print("Your guess is lesser.")
print("You got it right in", guess_num, "guesses.")