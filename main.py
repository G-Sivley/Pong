from turtle import Screen, Turtle
from paddle import Paddle


WIDTH = 800
HEIGHT = 600
BGCOLOR = "black"


# Step 1: Create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BGCOLOR)
screen.tracer(0)

# Listening Functions
screen.listen()


# Step 2: Create and move paddle
player = Paddle(-350)
screen.onkey(fun=player.move_up, key="w")
screen.onkey(fun=player.move_down, key="s")

# Step 3: create opponent paddle
opponent = Paddle(350)
screen.onkey(fun=opponent.move_up, key="Up")
screen.onkey(fun=opponent.move_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()

# Step 4: Create ball and make it move
# Step 5: collision with wall and bounce
# Step 6: detect collision with paddle
# step 7: detect when paddle misses
# step 8: Keep score


screen.exitonclick()