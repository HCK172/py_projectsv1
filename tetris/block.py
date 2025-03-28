from turtle import Turtle
import random 

POSITION = [(20,0),(-20,0),(0,20),(20,20),(-20,20)]


class Block:
    def __init__(self): 
        self.segments = []
    

    def create_block(self):
        center = Turtle()
        center.shape("square")
        
        




        




block = turtle()
block.shape("square")

block1 = Turtle()
block1.shape("square")
block1.penup()
block1.goto(random.choice(POSITION))

block2 = Turtle()
block2.shape("square")
block2.penup()
block2.goto(random.choice(POSITION))

block3 = Turtle()
block3.shape("square")
block3.penup()
block3.goto(random.choice(POSITION))