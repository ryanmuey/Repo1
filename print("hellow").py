import turtle

# Create the turtle and set its properties
t = turtle.Turtle()
t.color("blue")
t.shape("turtle")

# Create the tree
t.penup()
t.goto(0, -150)
t.pendown()
t.left(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)

# Place the apples
apples = []
for i in range(4):
    apple = turtle.Turtle()
    apple.shape("circle")
    apple.color("red")
    apple.shapesize(0.5)
    apple.penup()
    apple.goto(t.xcor() + (i * 50), t.ycor() + 50)
    apples.append(apple)

# Move the turtle with the arrow keys
def move_up():
    t.setheading(90)
    t.forward(20)
    check_collision()

def move_down():
    t.setheading(270)
    t.forward(20)
    check_collision()

def move_left():
    t.setheading(180)
    t.forward(20)
    check_collision()

def move_right():
    t.setheading(0)
    t.forward(20)
    check_collision()

turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.listen()

def check_collision():
    for apple in apples:
        if abs(t.xcor() - apple.xcor()) < 10 and abs(t.ycor() - apple.ycor()) < 10:
            apple.color("")
            apples.remove(apple)
            break

turtle.mainloop()