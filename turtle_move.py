import turtle

turtle.shape('turtle')

def turtle_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def turtle_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def turtle_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def turtle_down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def restart():
    turtle.reset()


turtle.onkey(turtle_right, 'd')
turtle.onkey(turtle_up, 'w')
turtle.onkey(turtle_left, 'a')
turtle.onkey(turtle_down, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()
turtle.mainloop()
