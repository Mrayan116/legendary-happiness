import random
from turtle import *

speed(0)

# Grasss
bgcolor("aquamarine4")

# Sky
penup()
goto(-400, -100)
pendown()
color("midnightblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

# moon
moon = Turtle()
moon.shape("circle")
moon.color("white")
moon.penup()
moon.goto(300, 220)
moon.shapesize(7)

# star
def draw_star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()

# Randomly place stars in the sky with varying sizes
for _ in range(25):
    x = random.randint(-300, 350)
    y = random.randint(-100, 350)
    size = random.randint(1, 4)  # Adjust the range for different star sizes
    draw_star(x, y, size)

# Clouds animation
cloud1 = Turtle()
cloud1.shape("circle")
cloud1.shapesize(3)
cloud1.color("white")
cloud1.penup()
cloud1.goto(-270, 260)

cloud2 = Turtle()
cloud2.shape("circle")
cloud2.shapesize(3)
cloud2.color("white")
cloud2.penup()
cloud2.goto(-285, 240)

cloud3 = Turtle()
cloud3.shape("circle")
cloud3.color("darkgrey")
cloud3.shapesize(3)
cloud3.penup()
cloud3.goto(-255, 240)

clouds = [cloud1, cloud2, cloud3]

# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("red", "darkgrey")  # (stroke, fill)
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# Chimney
penup()
goto(20, 130)
pendown()
color("orange", "firebrick1")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# Window 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 1 Cross - Horizontal Line 
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

# Window 1 Cross - Vertical Line 
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# Window 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 2 Cross - Horizontal Line 
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# Window 2 Cross - Vertical Line 
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

# Door
penup()
goto(-40, -97)
pendown()
right(90)
color("yellow")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# Door Handle
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()



# Set up the keyboard bindings for moving the moon
def left():
    x = moon.xcor()
    x -= 10
    moon.setx(x)

def right():
    x = moon.xcor()
    x += 10
    moon.setx(x)

def up():
    y = moon.ycor()
    y += 10
    moon.sety(y)

def down():
    y = moon.ycor()
    y -= 10
    moon.sety(y)

# Set up the keyboard bindings
screen = Screen()
screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

# Function to move the clouds to the specified coordinates
def move_clouds():
    for cloud in clouds:
        x = cloud.xcor()
        y = cloud.ycor()
        x += 5  # Move clouds to the right
        cloud.goto(x, y)

    ontimer(move_clouds, 100)  # Schedule the next move_clouds() call after 100 milliseconds

# Initial call to start the animation loop
move_clouds()

hideturtle()
done()  # Remove exitonclick() to allow the program to run indefinitely
