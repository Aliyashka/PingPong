"""
For homework ping-pong home work, you have to implement an addon to the ping-pong game. The list of possible projects includes (but not limits to):
1. done Add more players with separate key binding and collisions between players.
2. almost done Add obstacles on the canvas with different shapes (rectangles or balls).
3. done Make a function for players' registration with a name and displays a table of records.
4. Add the possibility to increase the difficulty by adding balls during the game.
5. DONE Increase or decrease the speed of the ball over time and implement speed controls with keys.
6*. Add walls that disappear (similar to task 2, but obstacle reappears randomly on hit).
7*. Enable physics with ball-pad friction and ball rotation.
8*. Write a bot not too hard, and not too easy: it makes mistakes and imitates the human's behavior.
"""

from models.GameScreen import GameScreen
from models.Pad import Pad
from managers.CollisionManager import CollisionManager
from managers.EventManager import EventManager
from models.HitBall import HitBall
from models.Obstalce import Obstacle

gameScreen = GameScreen()
players = [Pad(Pad.LEFTSIDE, "W", "S", "Aliya"),
           Pad(Pad.RIGHTSIDE, "Up", "Down", "Sasha"),
           Pad(Pad.RIGHTSIDE, "E", "D", "Dinara")]

gameScreen.drawSketch(players)
obstacles = [Obstacle(200, -110), Obstacle(-200, -150)]


def onWin(players, event):
    for i in players:
        if i.initSide == Pad.LEFTSIDE and event == EventManager.EVENT_GOAL_RIGHT or \
                i.initSide == Pad.RIGHTSIDE and event == EventManager.EVENT_GOAL_LEFT:
            i.score += 1
    # Redraw score
    gameScreen.drawSketch(players)


eventManager = EventManager()
eventManager.registerCallback(lambda event: onWin(players, event), EventManager.EVENT_GOAL_LEFT)
eventManager.registerCallback(lambda event: onWin(players, event), EventManager.EVENT_GOAL_RIGHT)
hitBalls = [HitBall(eventManager), HitBall(eventManager), HitBall(eventManager)]

collisionManager = CollisionManager(players, hitBalls, obstacles)

while 1:
    gameScreen.update()
    collisionManager.update()

    for hitBall in hitBalls:
        hitBall.update()

