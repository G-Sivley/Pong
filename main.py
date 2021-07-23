from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


WIDTH = 800
HEIGHT = 600
BGCOLOR = "black"


# Step 1: Create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BGCOLOR)
screen.tracer(0)

scoreboard = Scoreboard()

# Listening Functions
screen.listen()


# Step 2: Create and move paddle
l_paddle = Paddle(-350)
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# Step 3: create r_paddle paddle
r_paddle = Paddle(350)
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")


# Step 4: Create ball and make it move
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# Step 5: collision with wall and bounce
    if abs(ball.y_pos) > 285:
        ball.bounce_y()
        
# Step 6: detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.x_dir *= 1.1
        ball.y_dir *= 1.1
  
# step 7: detect when paddle misses
    if ball.xcor() > 400:
        scoreboard.r_point()
        ball.reset_ball()
    
    elif ball.xcor() < -400:
        scoreboard.l_point()
        ball.reset_ball()
    
# step 8: Keep score


screen.exitonclick()