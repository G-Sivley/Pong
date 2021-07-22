from turtle import Turtle

# Make Paddle class
class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        
        # Makes a stretched white box to emulate a pong paddle
        self.y_pos = 0
        self.x_pos = x_pos
        self.penup()
        self.speed(0)
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.goto(x=self.x_pos, y=self.y_pos)
        self.color("white") 
        
    def move_up(self):
        self.y_pos += 20
        self.goto(self.x_pos, self.y_pos)
    
    def move_down(self):
        self.y_pos -= 20
        self.goto(self.x_pos, self.y_pos)
    
    
    def move_down(self):
        self.backward(5)
    