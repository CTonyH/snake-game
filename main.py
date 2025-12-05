from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
square_list = []
x_position = 0


for _ in range(3):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.goto(y=0, x=x_position)
    new_turtle.turtlesize(0.5)
    new_turtle.shape("square")
    new_turtle.color("white")
    square_list.append(new_turtle)
    x_position += -10

























screen.exitonclick()
