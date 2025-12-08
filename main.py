from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
from PIL.ImageOps import posterize

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """Collision with food and Snake"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.add_score()
    """Collision with border"""
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        scoreboard.game_over()

    """Collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()
