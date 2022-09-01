from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "space")
screen.onkeypress(l_paddle.go_down, "b")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 21 or scoreboard.r_score == 21:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()