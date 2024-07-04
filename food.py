from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.set_new_position()
    def set_new_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)