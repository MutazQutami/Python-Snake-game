from turtle import Turtle

class Board(Turtle):
   def __init__(self):
       super().__init__()
       self.score=0
       self.high_score=self.get_high_score()
       self.shape("square")
       self.hideturtle()
       self.penup()
       self.speed("fastest")
       self.color("white")
       self.goto(0,260)
       self.write(f"Score: {self.score}  high_score:{self.high_score}", align="center", font=("Cooper Black", 20))

   def print_Score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}  high_score:{self.high_score} ", align="center", font=("Cooper Black", 20))

   def reset(self):

       if self.score > self.high_score:
           self.high_score = self.score
       self.save_high_score()
       self.score=0
       self.print_Score()

   def get_high_score(self):
       with open("high_score.txt", mode="r") as file:
           high_score=file.read()
           high_score=int(high_score)
       return high_score
   def save_high_score(self):
       with open("high_score.txt", mode="w") as file:
        file.write(str(self.high_score))

