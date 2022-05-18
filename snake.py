import turtle
import time
import random
d = 0.8
sc = 0
hc = 0
level=0
count1=0
count2=0
count3=0
count4=0
sp=0.15
w= turtle.Screen()
w.title("Snake Game")
w.bgcolor("blue")
w.setup(width=600, height=600)
w.tracer(0)
h = turtle.Turtle()
h.shape("turtle")
h.color("black")
h.penup()
h.goto(0, 0)
h.direction = "Stop"
f = turtle.Turtle()
c = "white"
s = "circle"
f.speed(0)
f.shape(s)
f.color(c)
f.penup()
f.goto(0, 100)
p= turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("red")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Score : 0 High Score : 0 Level:0", align="right",
		font=("Arial Narrow", 12, "bold"))
def goup():
	if h.direction != "down":
		h.direction = "up"
def godown():
	if h.direction != "up":
		h.direction = "down"
def goleft():
	if h.direction != "right":
		h.direction = "left"
def goright():
	if h.direction != "left":
		h.direction = "right"
def snake_game():
	if h.direction == "up":
		y = h.ycor()
		h.sety(y+20)
	if h.direction == "down":
		y = h.ycor()
		h.sety(y-20)
	if h.direction == "left":
		x = h.xcor()
		h.setx(x-20)
	if h.direction == "right":
		x = h.xcor()
		h.setx(x+20)
w.listen()
w.onkeypress(goup, "8")
w.onkeypress(godown, "2")
w.onkeypress(goleft, "4")
w.onkeypress(goright, "6")
l = []
while True:
	w.update()
	if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
		time.sleep(1)
		h.goto(0, 0)
		h.direction = "Stop"
		c = "black"
		s = "circle"
		for i in l:
			i.goto(1000, 1000)
		l.clear()
		sc = 0
		d = 0.8
		sp=0.175
		level=0
		count1=0
		count2=0
		count3=0
		count4=0
		p.clear()
		p.write("Score : {} High Score : {} Level:{} ".format(
			sc, hc,level), align="left", font=("Arial Narrow", 12, "bold"))
	if h.distance(f) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		f.goto(x, y)
		nl = turtle.Turtle()
		nl.speed(0)
		nl.shape("circle")
		nl.color("black") 
		nl.penup()
		l.append(nl)
		d -= sp
		sc += 10
		if sc > hc :
			hc = sc
		p.clear()
		if sc>=40 and sc <80 and count1!=1:
		    level=1
		    d=0.6
		    sp=0.1
		    count1=1
		if sc>=80 and sc <120 and count2!=1:
		    level=2
		    d=0.2
		    sp=0.025
		    count2=1
		if sc>=120 and sc <240 and count3!=1:
		    level=3
		    d=0.1
		    sp=0.001
		    count3=1
		if sc>=240 and count4!=1:
		    level=4
		    d=0.001
		    sp=0.0001
		    count4=1
		p.write("Score : {} High Score : {} Level:{} ".format(
			sc, hc,level), align="left", font=("Arial Narrow", 12, "bold"))
	for i in range(len(l)-1, 0, -1):
		x = l[i-1].xcor()
		y = l[i-1].ycor()
		l[i].goto(x, y)
	if len(l) > 0:
		x = h.xcor()
		y = h.ycor()
		l[0].goto(x, y)
	snake_game()
	for i in l:
		if i.distance(h) < 20:
			time.sleep(1)
			h.goto(0, 0)
			h.direction = "stop"
			c ="black"
			s ="circle"
			for i in l:
				i.goto(1000, 1000)
			i.clear()

			sc = 0
			d = 0.1
			level=0
			count1=0
			count2=0
			count3=0
			count4=0
			p.clear()
			p.write("Score : {} High Score : {} Level:{} ".format(
				sc, hc,level), align="left", font=("Arial Narrow", 12, "bold"))
	time.sleep(d)

w.mainloop()
