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

t.backward(50)
t.circle(50)
t.fillcolor('black')
t.begin_fill()
t.circle(25)
t.end_fill()

t.forward(200)
t.circle(50)
t.fillcolor('black')
t.begin_fill()
t.circle(25)
t.end_fill()

t.backward(125)

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.penup()
t.goto(50,-150)
t.pendown()
t.circle(150)

t.penup()
t.goto(-50,-50)
t.setheading(270)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(100,180)
t.left(90)
t.forward(200)
t.end_fill()
