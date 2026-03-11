from snake import Snake
from turtle import Screen
import time
from food import Food
from score_board import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
board=ScoreBoard()

body=Snake()
bite=Food()
game_over=False
screen.onkey(body.up,"w")
screen.onkey(body.down,"s")
screen.onkey(body.right,"d")
screen.onkey(body.left,"a")
while not game_over:
    screen.update()
    time.sleep(0.1)
    body.move()
    if(body.head.distance(bite.position())<=15):
        bite.spawn()
        body.increase_length()
        board.increase_score()

    if(body.head.xcor()>300 or body.head.xcor()<-300 or body.head.ycor()>300 or body.head.ycor()<-300):
        game_over=True
        board.game_over()
    
    for seg in range(1,len(body.segments),1):
        if(body.head.distance(body.segments[seg].position())<19):
            game_over=True
            board.game_over()

screen.exitonclick()
