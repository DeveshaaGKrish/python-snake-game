from turtle import Turtle
from random import randint

class Food(Turtle):
    '''Turtle as food to snake'''
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color("#19E20E")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.update_food()

    def update_food(self):
        food_position = (randint(-280, 280), randint(-280, 250))
        self.setheading(randint(0, 360))
        self.goto(food_position)