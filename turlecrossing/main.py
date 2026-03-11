from turtle import Turtle,Screen
from cars import Car
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.listen()
screen.tracer(0)

tim=Turtle("turtle")
tim.penup()
tim.xcor=0
tim.ycor=-280
tim.goto(tim.xcor,tim.ycor)
tim.setheading(90)
def move_forward():
    tim.ycor += 10
    tim.goto(tim.xcor,tim.ycor)

move_speed=0.1
game_over=False
car_list=[]
i=0
screen.onkeypress(move_forward,"w")
while not game_over:
    time.sleep(move_speed)
    screen.update()
    if(i%9==0):
        new_car=Car()
        car_list.append(new_car)
    for cars in car_list:
        if(tim.distance(cars)<20):
            game_over=True
        cars.move()

    if(tim.ycor==280):
        move_speed *= 0.9
        tim.teleport(0,-280)
        tim.ycor=-280

    i+=1




screen.exitonclick()

