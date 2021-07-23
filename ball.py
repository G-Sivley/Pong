from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.x_pos = 0
        self.y_pos = 0
        self.x_dir = 10
        self.y_dir = 10
        self.penup()
        self.shape("circle")
        self.color("white")
    
    def move(self):
        # Change the current postion by the current x or y direction
        self.x_pos += self.x_dir
        self.y_pos += self.y_dir
        self.goto(x=self.x_pos, y=self.y_pos) 
    
    def bounce_y(self):
        self.y_dir *= -1
        
    def bounce_x(self):
        self.x_dir *= -1
        
    
    def reset_ball(self):
        self.x_pos = 0
        self.y_pos = 0
        self.x_dir = 10
        self.y_dir = 10
        self.bounce_x() 