from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.display_score()

    def display_score(self):
        display_text = f"Score: {self.score}"
        self.write(arg=display_text, move=False, align='center', font=('Comic Sans MS', 16, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        display_text = f"Game Over"
        self.goto(0,0)
        self.write(arg=display_text, move=False, align='center', font=('Comic Sans MS', 16, 'normal'))