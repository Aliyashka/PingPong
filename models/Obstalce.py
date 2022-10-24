import turtle
from random import randint

class Obstacle():
    turt = None
    width = 5
    height = 5
    correctMultipler = 13

    def __init__(self, x, y):
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        #self.triangle()

        if randint(0, 1):
            self.ball()
        else:
            self.rectangle()

        self.turt.goto(x, y)

    def rectangle(self):
        self.turt.shape("square")
        self.turt.color("green")
        self.turt.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.turt.penup()

    # TODO: something is wrong with drawing
    def triangle(self):
        t = self.turt
        t.fillcolor("red")

        # start the filling color
        t.begin_fill()

        # drawing the triangle of side s
        for _ in range(3):
            t.forward(50)
            t.right(-120)

        # ending the filling of the color
        t.end_fill()
        t.penup()

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