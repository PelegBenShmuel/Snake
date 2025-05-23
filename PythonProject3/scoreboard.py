from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couruer",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("../../Desktop/data.txt") as data:
             self.high_score = int(data.read())
        self.hideturtle()
        self.goto(-10,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}",align= ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("C:/Users/peleg/Desktop/data.txt",mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
