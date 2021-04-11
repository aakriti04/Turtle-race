from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,500)
user_inp = screen.textinput(title="Make bet", prompt="Fill you bet turtle color: ")
turtle_colors = ["red", "green", "blue", "pink", "yellow", "orange"]
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_inp:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 because each turtle width is 40 and last coordinate is 250. Therefore winning coordinate is 250-(40/2)
        if turtle.xcor()>230:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_inp:
                print(f"You have won the bet. Winning Turtle Color is {winning_turtle_color}")
            else:
                print(f"You have lost the bet. Winning Turtle Color is {winning_turtle_color}")
        dist = random.randint(0,10)
        turtle.forward(dist)


screen.exitonclick()