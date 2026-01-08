from os import write
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=275)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
            # self.write_data(self.score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    # def read_data(self):
    #     with open("data.txt", mode="r") as file:
    #         high_score = int(file.read())
    #         return high_score
    #
    # def write_data(self, new_highscore):
    #     with open("data.txt", mode="w") as file:
    #         file.write(f"{new_highscore}")
