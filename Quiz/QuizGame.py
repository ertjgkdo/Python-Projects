print("Welcome to my quiz")
global score
score = 0
def start(question, answer):
    global score
    user_answer = input(question)
    if user_answer.strip().lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        

question1 ="What does CPU stand for? "
question2 ="What does ROM stand for? "
question3 ="What does GPU stand for? "
question4 ="What does PSU stand for? "

answer1 = "central processing unit"
answer2 = "read only memory"
answer3 = "graphic processing unit"
answer4 = "power supply unit"

playing = input("Do you want to play? ")
if playing.strip().lower() !="yes":
    quit()
print("Okay! Let's play :)")

start(question1, answer1)

start(question2, answer2)
start(question3, answer3)
start(question4, answer4)
print("End of Quiz")
print("You got " + str(score) + " questions right.")



