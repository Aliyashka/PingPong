class CollisionManager:
    collisionDistance = 80
    players = None
    hitBalls = None
    obstacles = None

    def __init__(self, players, hitBalls, obstacles):
        self.players = players
        self.hitBalls = hitBalls
        self.obstacles = obstacles

    def update(self):
        self.checkPlayersWithBalls()
        self.checkObstaclesWithBalls()

    def checkObstaclesWithBalls(self):
        for hitball in self.hitBalls:
            for obstacle in self.obstacles:
                # Сравнить между собой
                hitball.ball.ycor()
                hitball.ball.xcor()
                obstacle.turt.xcor()
                obstacle.turt.ycor()

    def checkPlayersWithBalls(self):
        # Check players collisions with the the balls
        for player in self.players:
            for hitball in self.hitBalls:
                ball = hitball.ball
                collisionDistance = self.collisionDistance

                # Ball collision with players paddles
                if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < player.ycor() + collisionDistance and ball.ycor() > player.ycor() - collisionDistance:
                    ball.setx(360)
                    hitball.dx *= -1

                if ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < player.ycor() + collisionDistance and ball.ycor() > player.ycor() - collisionDistance:
                    ball.setx(-360)
                    hitball.dx *= -1

