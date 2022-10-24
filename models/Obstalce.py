import turtle
from random import randint

class Obstacle():
    turt = None
    width = 5
    height = 5
    correctMultipler = 13

    def __init__(self,x,y):
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        #self.square()
        #self.rectangle()
        self.ball()
        self.turt.goto(x, y)

    def square(self):
        self.turt.shape("square")
        self.turt.color("green")
        self.turt.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.turt.penup()


    def rectangle(self, width, height):
        turtle = self.turt
        turtle.up()
        turtle.goto(50, 50)
        turtle.down()

    def ball(self):
        self.turt.shape("circle")
        self.turt.color("red")
        self.turt.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.turt.penup()
    #Appearance and dissapearance of obstilces
    def randomPosition(self):

        self.turt.goto(randint(-200,200), randint(-200, 200))

    #TODO
    def appear(self):
        turtle.showturtle()
    #TODO
    def dissapear(self):
        turtle.hideturtle()