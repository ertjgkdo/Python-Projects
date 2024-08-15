import turtle
import time
import random

#defining size for the turtle screen
WIDTH, HEIGHT = 500,500
COLORS = ['red', 'blue', 'green','black', 'yellow', 'orange', 'purple', 'brown']
def get_no_of_racers():
    no_of_racers = 0
    #in order for the question to be asked until the user enters valid input
    while True:
        no_of_racers = input("Enter the number of turtles for the race (2-8): ")
        if no_of_racers.isdigit():
            no_of_racers = int(no_of_racers)
        else:
            print("Please enter a numeric value.")
            continue

        if 2<= no_of_racers <=8:
            return no_of_racers
        else:
            print("The race is possible between 2-8 turtles only. Pick a number in the range!")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH //(len(colors) + 1)
    for i, color in enumerate(colors):
        newturtle = turtle.Turtle()
        newturtle.color(color)
        newturtle.shape('turtle')
        newturtle.left(90)
        newturtle.penup()
        newturtle.setpos(-WIDTH//2 + (i +1) * spacingx, -HEIGHT//2 + 20)
        newturtle.pendown()
        
        turtle.done()
        turtles.append(newturtle)
    return turtles  

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for newturtle in turtles:
            distance = random.randrange(1,20)
            newturtle.forward(distance)
            x,y = newturtle.pos()
            if y>= HEIGHT//2 -10:
                return colors[turtles.index(turtle)]

def init_turtle():
    #creating the screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Race') 

racers = get_no_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner)



