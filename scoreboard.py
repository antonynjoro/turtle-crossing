from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("light slate gray")
        self.goto(-230, 270)
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
        self.goto(0, -30)
        self.write(f"Press 'y' to start a new game", align="center", font=FONT)
