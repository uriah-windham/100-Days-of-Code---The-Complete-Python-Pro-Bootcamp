from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.tail = self.snake_list[len(self.snake_list) - 1]
        self.old_x = 0
        self.old_y = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_list.append(snake)

    def extend_snake(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        self.old_x = self.tail.xcor()
        self.old_y = self.tail.ycor()

        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_backward(self):
        for seg_num in range(0, len(self.snake_list) - 1):
            new_x = self.snake_list[seg_num + 1].xcor()
            new_y = self.snake_list[seg_num + 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.tail.goto(self.old_x, self.old_y)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

