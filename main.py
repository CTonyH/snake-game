from turtle import Screen, Turtle

from PIL.ImageOps import posterize

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
segment_positions = ((0,0), (-20, 0), (-40, 0))



for position in segment_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)

























screen.exitonclick()
