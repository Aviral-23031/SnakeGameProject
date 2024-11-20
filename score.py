from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        with open("Data.txt") as data:
            self.highscore=int(data.read())
        self.score = 0
        self.goto(-10,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def score_change(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0