from turtle import Screen
import time
from snake import Snake
from food import Food
from scorecard import ScoreCard



screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()


screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

    
game_is_on = True 
score_card = ScoreCard()  

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food.
    if snake.head.distance(food) < 30:
        food.refresh()
        score_card.increase_score()
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        score_card.game_over()


    
screen.exitonclick()




# goal: detect collision with food.  Should be able to hit a piece of food (blue circle).  whenever the snake touches the food, the food will move to a new random location.


# write some text in the program that keeps track of the score of how many pieces of food we've managed to eat.  The score updates every time we hit a new piece of food. The scoreboard is also going to be a turtle.

# 


    
    

