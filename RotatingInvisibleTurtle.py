# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:41:30 2023

@author: riyam
"""

import turtle
t=turtle.getscreen()
t1=turtle.Turtle()
turtle.hideturtle()
t.title("Rotating Turtle")

t1.pencolor("yellow")
t1.shapesize(10,10,10)

t1.shape("turtle")
for angle in range(0,901,90):
    t1.lt(angle)
t1.ht()    