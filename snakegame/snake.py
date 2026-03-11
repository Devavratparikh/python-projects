from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]

    def createsnake(self):
        positions=[(0,0),(-20,0),(-40,0)]
        for position in positions:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if(self.head.heading()==270):
            return
        self.head.setheading(90)

    def down(self):
        if(self.head.heading()==90):
            return
        self.head.setheading(270)

    def right(self):
        if(self.head.heading()==180):
            return
        self.head.setheading(0)

    def left(self):
        if(self.head.heading()==0):
            return
        self.head.setheading(180)

    def increase_length(self):
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.segments[-1].position())
            self.segments.append(new_segment)



    