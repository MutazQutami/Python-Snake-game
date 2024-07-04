from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVER_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.build_the_snake_body()
        self.head="Right"

    def build_the_snake_body(self):
        for position in STARTING_POSITIONS:
            square = Turtle(shape='square')
            square.color("white")
            square.penup()
            square.goto(position)
            self.snake_body.append(square)
    def grow_up(self):
       square=Turtle(shape="square")
       square.color("white")
       square.penup()
       position_of_last_one=self.snake_body[-1].pos()
       square.goto(position_of_last_one)
       self.snake_body.append(square)
    def move(self):
        for square in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[square - 1].xcor()
            new_y = self.snake_body[square - 1].ycor()
            self.snake_body[square].goto(new_x, new_y)
        self.snake_body[0].forward(MOVER_DISTANCE)

    def move_up(self):
            if(self.head!="Up" and self.head!="Down"):
                self.snake_body[0].setheading(90)
                self.head="Up"


    def move_down(self):
            if(self.head!="Up"and self.head!="Down"):
                 self.snake_body[0].setheading(270)
                 self.head="Down"

    def move_left(self):
           if(self.head!="Left" and self.head!="Right"):
               self.snake_body[0].setheading(180)
               self.head="Left"

    def move_right(self):
           if(self.head!="Left"and self.head!="Right"):
              self.snake_body[0].setheading(0)
              self.head="Right"

    def snake_clear(self):
        for square in self.snake_body:
            square.hideturtle()
        self.snake_body.clear()
        self.build_the_snake_body()
        self.head = "Right"