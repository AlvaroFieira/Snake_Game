from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.obtain_last_high_score()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.display_score()

    def obtain_last_high_score(self):
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())

    def display_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()
