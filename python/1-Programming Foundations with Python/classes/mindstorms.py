# first: install library :	
# 		sudo apt-get install python-tk

import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	j = 0
	while j < 3:
		some_turtle.forward(100)
		some_turtle.left(120)
		j += 1
			

def draw():
	window = turtle.Screen()
	window.bgcolor("red")
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(3)
	draw_square(brad)

	angle = turtle.Turtle()
	angle.shape("arrow")
	angle.color("blue")
	angle.circle(100)
	
	trian = turtle.Turtle()
	trian.shape("triangle")
	trian.left(180)
	draw_triangle(trian)
	
	window.exitonclick()

draw()
