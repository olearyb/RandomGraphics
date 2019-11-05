import math
import random
from graphics import *

# create the graphwin object
canvas = GraphWin("Random Graphics", 1000, 700)
canvas.setBackground("light goldenrod")
w, h = canvas.getWidth(), canvas.getHeight()

'''-----------------------COLOR PALLETTES ----------------------'''

colors = ["#03CDD2", "#A26DCB", "#FB7299"]
rainySeason = ["#3BABFD", "#6DC1FF", "#B2DDFF", "#06CDF4", "#224B8B"]
## https://www.schemecolor.com/rainy-season.php
fadedFreedom = ["#BB3A69", "#DD7179", "#EEE7C7", "#68C6BC", "#2C95A5"]
## schemecolor.com/faded-freedom.php
neonGradient = ["#14F2E0", "#41C8E5", "#6E9EEB", "#C74BF6", "#F320FA"]
## https://www.schemecolor.com/aqua-pink-gradient.php
bouncing = ["#F25E74", "#FF8884", "#026178", "#0682A6", "#34A1C7"]
## https://www.schemecolor.com/bouncing.php
beachThings = ["#EB6489", "#F8EFB8", "#F9E07D", "#70D280", "#3C8CDE", "#4AD5FF"]
## https://www.schemecolor.com/beach-things.php

'''---------------------------FUNCTIONS------------------------'''
# functions to draw random cirlces of a certain color pallete 
def rainy(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        circle.setFill(random.choice(rainySeason))
        circle.draw(canvas)
    #endfor
#end rainy


def freedom(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        circle.setFill(random.choice(fadedFreedom))
        circle.draw(canvas)
    #endfor
#end freedom

def neon(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        circle.setFill(random.choice(neonGradient))
        circle.draw(canvas)
    #endfor
#end neonCircles

def bouncing(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        circle.setFill(random.choice(bouncing))
        circle.draw(canvas)
    #endfor
#end bouncing
        
def beach(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        circle.setFill(random.choice(beachThings))
        circle.draw(canvas)
    #endfor
#end beach
        
        
        
