from turtle import Turtle
import random
import time

START_X_POS = [+570, -570]
START_Y_POS = [+100, -100]

class Ball:
    def __init__(self, move_distance=20, last_point = 0):
        self.move_distance = move_distance
        self.last_point = last_point
        self.angle = (random.randint(-66, +66))
        self.initial_position = (random.choice(START_X_POS), random.choice(START_Y_POS))
        self.hitwall = 0
        if self.initial_position[0] < 0:
            self.direction = 1
        else:
            self.direction = 0
        self.create_ball()
        self.collision = False
        self.x = self.ball.position()[0]
        self.y = self.ball.position()[1]

    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(self.initial_position)
        self.ball.setheading(self.angle)

    def reset_ball(self):
        self.ball.goto(START_X_POS[self.last_point], random.choice(START_Y_POS))
        self.angle(random.randint(-66, +66 ))
        self.ball.setheading(self.angle)


    def is_collision(self):
        print(self.x)
        if self.x > 575 or self.x < -575:
            self.collision = True


    def move(self):
        self.x = self.ball.position()[0]
        self.y = self.ball.position()[1]

       # print(self.angle, self.ball.position()[0], self.ball.position()[1])
        if self.hitwall is False:
            if self.y > 265 or self.y < -265:
                self.hitwall = True
                if self.angle > 0:
                    self.angle -= 90
                else:
                    self.angle += 90
        else:
            self.hitwall = False
        self.ball.setheading(self.angle)
        if self.direction == 1:
            self.ball.forward(self.move_distance)
        else:
            self.ball.backward(self.move_distance)
        self.is_collision()