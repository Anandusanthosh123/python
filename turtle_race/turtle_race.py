import turtle
import time
import random


WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'brown', 'black', 'purple', 'pink', 'cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is numeric ... Try Again!")
            continue  # immediately brings back to while loop

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            # either move turtle between 1 or 20px
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():

    screen = turtle.Screen()  # intializing turtle screen
    screen.setup(WIDTH, HEIGHT)  # setup screen
    screen.title("Turtle Racing!")  # change title


racers = get_number_of_racers()


init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner of Race is {winner} Turtle!")
time.sleep(5)
