from turtle import Turtle
import time

UP = 90
DOWN = 270




PAUSE_KEYPRESSED = 10

class Paddle:
    def __init__(self, initial_position, move_distance=20, initial_size=3 ):
        self.paddle: [Turtle] = []
        self.initial_position = initial_position
        self.initial_items = initial_size
        self.move_distance = move_distance
        self.create_paddle()
        self.is_moving = False
        self.head = self.paddle[0]
        self.head.setheading(UP)
        self.time_last_key_pressed = 0

    def create_paddle(self):
        for _ in range(self.initial_items):
            self.add_to_paddle()



    def add_to_paddle(self):
        paddle_item = Turtle()
        paddle_item.shape("square")
        paddle_item.color("white")
        paddle_item.penup()
        paddle_item.goto(self.initial_position)

        if len(self.paddle) > 0:
            last_item: Turtle = self.paddle[-1]
            x = last_item.position()[0]
            y = last_item.position()[1] - 20
            paddle_item.setpos(x, y)


        self.paddle.append(paddle_item)

    def move_paddle(self):
        # range (start <- included, stop <-- not included, step)
        if ( self.head_position()[1] >= 0 and self.head_position()[1] <= 280 )  or ( self.head_position()[1] <= 0 and self.head_position()[1] >= -280) :
            for index in range(len(self.paddle) - 1, -1, -1):
                current_paddle_item = self.paddle[index]
                if index == 0:
                    current_paddle_item.forward(self.move_distance)
                else:
                    new_pos: (float, float) = (self.paddle[index - 1].pos()[0], self.paddle[index - 1].pos()[1])
                    current_paddle_item.setpos(new_pos)
        else:
            if self.is_moving == True:
                self.stop_paddle()
    def stop_paddle(self):
        self.is_moving = False

    def collision(self):
        for paddle_item in self.paddle[1:]:
            return self.head.distance(paddle_item) <= 10
        return False

    def turn_up(self):
        if self.head.heading() == DOWN:
            print(f"Paddle: {self.paddle[0].pos()}")
            self.paddle.reverse()
            print(f"Paddle:  {self.paddle[0].pos()}")
            self.head = self.paddle[0]
        self.head.setheading(UP)
        print(f"Paddle: {self.paddle[0].pos()}")
        self.is_moving = True

    def turn_down(self):
        if self.head.heading() == UP:
            print(f"Paddle: {self.paddle}")
            self.paddle.reverse()
            print(f"Paddle: {self.paddle}")
            self.head = self.paddle[0]
        self.head.setheading(DOWN)
        print(self.head.heading())
        self.is_moving = True



    def head_position(self):
        return self.head.position()