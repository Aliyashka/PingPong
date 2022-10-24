import turtle
from models.GameScreen import GameScreen


class Pad():
    distance = 20
    score = 0
    turt = None
    LEFTSIDE = -400
    RIGHTSIDE = 400
    name = None
    initSide = None

    def __init__(self, initSide, up, down, name):
        self.name = name
        self.initSide = initSide

        self.turt = turtle.Turtle()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.shapesize(stretch_wid=6, stretch_len=2)
        self.turt.penup()
        self.turt.goto(initSide, 0)

        GameScreen.bindKeys(self.moveup, up)
        GameScreen.bindKeys(self.movedown, down)

    def moveup(self):
        self.turt.sety(self.turt.ycor() + self.distance)

    def movedown(self):
        self.turt.sety(self.turt.ycor() - self.distance)

    def xcor(self):
        return self.turt.xcor()

    def ycor(self):
        return self.turt.ycor()
