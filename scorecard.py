from turtle import Turtle
from food import Food


ALIGNMENT = 'center'
font_size = 24
FONT = ("courier", font_size, "normal")

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()
       

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += 5
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game-Over! Final Score: {self.score}", align=ALIGNMENT, font=FONT )
        







        

        
        




      

        
    
