from turtle import Turtle
INITIAL_POSITIONS = [(-20*x, 0) for x in range(3)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    '''Snake creation and movements'''
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
    
    def create_snake(self):
        for position in INITIAL_POSITIONS:
             self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle('circle')
        segment.penup()
        segment.color("#BC0EE2")
        segment.goto(position)
        self.all_segments.append(segment)
    
    def grow(self):
        last_segment_position = self.all_segments[-1].position()
        self.add_segment(last_segment_position)

    def move(self):
        for segement_num in range(len(self.all_segments)-1,0, -1):
            tail = self.all_segments[segement_num]
            tail_but_one = self.all_segments[segement_num-1]
            new_x = tail_but_one.xcor()
            new_y = tail_but_one.ycor()
            tail.goto((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)