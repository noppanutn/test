import turtle as t

t.speed(0)

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.fillcolor("yellow")
t.backward(50)
t.circle(50)
t.begin_fill()
t.circle(25)
t.end_fill()
t.forward(200)
t.circle(50)
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(50,-200)
t.pendown()
t.circle(200)

t.fillcolor('red')
t.penup()
t.goto(-50,-50)
t.pendown()
t.begin_fill()
t.setheading(270)
t.circle(100,180)
t.left(90)
t.forward(200)
t.end_fill()
