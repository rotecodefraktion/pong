from ball import Ball
from turtle import Screen, Turtle
from paddle import Paddle
import random

import time

SCREENSIZE = (1200,600)

PADDLE_POS_X = {"left":int(SCREENSIZE[0]/-2 + 30),
                "right":int(SCREENSIZE[0]/2 - 30)}

#print(PADDLE_POS_X["left"], PADDLE_POS_X["right"])

screen = Screen()
screen.setup(width=SCREENSIZE[0], height=SCREENSIZE[1])
screen.title("The ultimate PONG")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


def net_line():
    screen_height = int(SCREENSIZE[1] / 2) - 30
    net = Turtle()
    net.color("white")
    net.penup()
    net.shape("square")
    net.shapesize(0.2,0.60)
    net.goto(0, screen_height)
    net.setheading(270)
    while net.position()[1] > int(SCREENSIZE[1] / -2) + 20:
        print(net.position())
        net.stamp()
        net.forward(25)



net_line()
paddle_left = Paddle(initial_size=4, initial_position=(PADDLE_POS_X["left"], 40))
paddle_right = Paddle(initial_size=4, initial_position=(PADDLE_POS_X["right"], 40))
ball = Ball()

screen.update()



screen.onkeypress(paddle_left.turn_up, "w")
screen.onkeyrelease(paddle_left.stop_paddle, "w")
screen.onkeypress(paddle_right.turn_up, "Up")
screen.onkeyrelease(paddle_right.stop_paddle, "Up")
screen.onkeypress(paddle_left.turn_down, "s")
screen.onkeyrelease(paddle_left.stop_paddle, "s")
screen.onkeypress(paddle_right.turn_down, "Down")
screen.onkeyrelease(paddle_right.stop_paddle, "Down")

while True:
    if paddle_left.is_moving:
        paddle_left.move_paddle()
    if paddle_right.is_moving:
        paddle_right.move_paddle()
    time.sleep(0.1)
    ball.move()
    print(f"{ball.collision}")
    if ball.collision == True:
        exit()
    print(f"{paddle_left.head.distance(100,100)}")


    for i in range(0, len(paddle_left), 1):
        if paddle_left[i].distance(ball) > 15:
            ball.direction = 1
            break
        else:
            ball.direction = 0

    screen.update()


screen.exitonclick()