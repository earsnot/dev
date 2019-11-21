import turtle
import random

silly = turtle.Turtle()
silly.speed(70)
silly.penup()
silly.setpos(-400,-250)
silly.pendown()
random.randrange(0,15)


def filler(color):
    silly.begin_fill()

    for i in range(0,2):
	    silly.forward(800)
	    silly.right(90)
	    silly.forward(200)
	    silly.right(90)
    silly.color(color)
    silly.end_fill()
    pass

silly.color("black")

for x in range(0,1):
    filler("red")
    pass
turtle.done()
#silly.forward(150)
#
#for x in range(1,21):
#	
#	for i in range(1,11):
#		if i == 3 and x < 15 or i == 4 and x < 15:
#			silly.begin_fill()
#			silly.color("brown")
#			silly.left(90)
#			silly.forward(10)
#			silly.right(90)
#			silly.forward(50)
#			silly.right(90)
#			silly.forward(10)
#			silly.left(90)
#			silly.end_fill()
#			silly.color("black")
#		elif i == 8 and x > 7 and x < 15 or i == 9 and x > 7 and x < 15 :
#			silly.begin_fill()
#			silly.color("#A9CCE3")
#			silly.left(90)
#			silly.forward(10)
#			silly.right(90)
#			silly.forward(50)
#			silly.right(90)
#			silly.forward(10)
#			silly.left(90)
#			silly.end_fill()
#			silly.color("black")
#
#		else:
#			silly.begin_fill()
#			silly.left(90)
#			silly.forward(10)
#			silly.right(90)
#			silly.forward(50)
#			silly.right(90)
#			silly.forward(10)
#			silly.left(90)
#			silly.color("orange")
#			silly.end_fill()
#			silly.color("black")
#
#	silly.left(90)
#	silly.forward(10)
#	silly.right(90)
#	silly.penup()
#	silly.forward(-500)
#	silly.pendown()
#
#silly.begin_fill()
#silly.color("#6E2C00")
#silly.left(60)
#silly.forward(100)
#silly.right(60)
#silly.forward(400)
#silly.right(60)
#silly.forward(100)
#silly.left(60)
#silly.end_fill()
#silly.color("black")
#
#silly.penup()
#silly.forward(-100)
#silly.left(90)
#silly.forward(30)
#silly.pendown()
#
#silly.begin_fill()
#for i in range(1,3):
#	silly.forward(70)
#	silly.left(90)
#	silly.forward(30)
#	silly.left(90)
#silly.end_fill()
#
#silly.forward(70)
#silly.left(90)
#silly.forward(15)
#silly.right(90)
#
#tpos = silly.pos()
#
#for x in range(1,11):
#	
#	for i in range(1,50):
#		silly.circle(random.randrange(0,15),random.randrange(30,240))
#	silly.penup()
#	silly.goto(tpos[0],tpos[1])	
#	silly.pendown()
#turtle.done()
