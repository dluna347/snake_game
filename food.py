from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

        
        
        



















# will know how to render itself as a small circle on the screen.  Food gets touched, food moves to random location

# how can we detect when the food and the snake have come into contact
# and then have the food move to a new random location