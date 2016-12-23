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
	brad.speed(5)
	
	for i in range(1, 37):
		draw_square(brad)
		brad.right(10)

	
	trian = turtle.Turtle()
	trian.shape("triangle")
	trian.forward(300)
	trian.speed(10)
	
	for i in range(1, 37):
		draw_triangle(trian)
		trian.left(10)
		
	cir = turtle.Turtle()
	cir.speed(12)
	cir.shape("circle")
	cir.left(180)
	cir.forward(400)
	
	for i in range(1, 37):
		cir.circle(100)
		cir.left(10)	
		
	window.exitonclick()

draw()
