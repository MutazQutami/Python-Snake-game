import time
from snake import Snake
from turtle import Screen
from food import Food
from score_board import Board

#Screen setup
my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)


#Declarations
snake = Snake()
food = Food()
board = Board()

#Keyboard control
my_screen.listen()
my_screen.onkey(snake.move_up,"Up")
my_screen.onkey(snake.move_down,"Down")
my_screen.onkey(snake.move_left,"Left")
my_screen.onkey(snake.move_right,"Right")


#Move the snake

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collison with food.
    if snake.snake_body[0].distance(food)<15:
        food.set_new_position()
        board.score+=1
        board.print_Score()
        snake.grow_up()

    #Detect collision with boarders
    x,y=snake.snake_body[0].pos()
    if x>290or x<-290  or y >290 or y <-290:
        board.reset()
        snake.snake_clear()

    #Dectect collision with tail
    for square in snake.snake_body[1:]:
        if snake.snake_body[0].distance(square)<10 :
            board.reset()
            snake.snake_clear()


my_screen.exitonclick()