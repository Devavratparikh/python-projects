import random 
from turtle import Turtle
import turtle
turtle.colormode(255)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.penup()
        self.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.x=370
        self.y=random.randint(-250,250)
        self.teleport(self.x,self.y)   

    def move(self):
        new_x=self.x
        new_x=new_x-5
        self.x=new_x
        self.goto(new_x,self.y)    