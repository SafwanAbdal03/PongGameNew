from turtle import Screen
from bat import TennisBat
from ball import Ball
from scoreboard import Scoreboard
import time

# Starting positions for the bats
LEFT_STARTING_POSTITION = (-270, 0)
RIGHT_STARTING_POSTITION = (270, 0)

#Initial time delay to control the speed
TIME = 0.05

#Sets up the screen
gameScreen = Screen()
gameScreen.setup(600, 400)
gameScreen.bgcolor("black")
gameScreen.title("Pong Game")

#Initiates the bat and ball objects and puts them in their positions
Left_Bat = TennisBat()
Right_Bat = TennisBat()
Ball = Ball()
scoreboard = Scoreboard()
Left_Bat.goto(LEFT_STARTING_POSTITION)
Right_Bat.goto(RIGHT_STARTING_POSTITION)

#Listens for player inputs
gameScreen.listen()
gameScreen.onkey(fun=Left_Bat.Move_Down, key="s")
gameScreen.onkey(fun=Left_Bat.Move_Up, key="w")
gameScreen.onkey(fun=Right_Bat.Move_Down, key="Down")
gameScreen.onkey(fun=Right_Bat.Move_Up, key="Up")

#Main game
if __name__ == "__main__":
    while True:
        time.sleep(TIME)
        gameScreen.update()
        Ball.move()
        if Ball.ycor() > 180 or Ball.ycor() < -180:
            Ball.bounce()
        #If the right side player misses, left side player gets a point and vise versa
        elif Ball.xcor() > 280:
            gameScreen.tracer(0)
            # Allowing the ball to go back to the center without being traced
            Ball.setposition(0, 0)
            Ball.x_bounce()
            TIME = 0.05
            gameScreen.tracer(1)
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            scoreboard.check_win(points=scoreboard.l_score, player="PLAYER 1")
            if scoreboard.l_score >= 10:
                gameScreen.exitonclick()
        elif Ball.xcor() < -280:
            gameScreen.tracer(0)
            Ball.setposition(0, 0)
            Ball.x_bounce()
            TIME = 0.05
            gameScreen.tracer(1)
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            scoreboard.check_win(points=scoreboard.r_score, player="PLAYER 2")
            if scoreboard.r_score >= 10:
                gameScreen.exitonclick()
        #Ensuring that the ball bounces regardless of the part of the bat it hits
        elif Ball.distance(Left_Bat) < 55 and Ball.xcor() < -250:
            Ball.x_bounce()
            TIME *= 2/3
        elif Ball.distance(Right_Bat) < 55 and Ball.xcor() > 250:
            Ball.x_bounce()
            TIME *= 2/3
