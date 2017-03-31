import turtle as t
import math as m
t.speed(0)

t.penup()
t.goto(0,-210)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(210)
t.end_fill()
t.penup()
t.goto(0,-200)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(200)
t.end_fill()


for i in range(4):
    t.fillcolor('black')
    t.begin_fill()
    t.forward(5)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(5)
    t.end_fill()
    t.circle(200,90)

for i in range(12):
    t.fillcolor('black')
    t.begin_fill()
    t.forward(5)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(5)
    t.end_fill()
    t.circle(200,30)

hour = t.Turtle()
hour.shape('square')
hour.shapesize(4,0.5)
hour.penup()


minute = t.Turtle()
minute.shape('square')
minute.shapesize(6,0.5)
minute.penup()

##for i in range(360):
##    minute.setheading(360-(90+i*6))
##    minute.goto(100*m.cos(m.radians(360-i*6)),100*m.sin(m.radians(360-i*6)))
##   
##    hour.setheading(360-(90+i))
##    hour.goto(100*m.cos(m.radians(360-i)),100*m.sin(m.radians(360-i)))

hour.setheading(180)
hour.goto(0,30)
minute.setheading(180)
minute.goto(0,50)
for i in range(720):
    hour.circle(30,-0.5)
    minute.circle(50,-6)
    #print(i)
    
    
