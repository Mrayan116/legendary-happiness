import turtle

def square(clr):
    t.pendown()
    t.fillcolor(clr)
    t.begin_fill()
    for x in range(4):
        t.forward(20)
        t.right(90)
    t.forward(20)
    t.end_fill()
    t.penup()
   
t = turtle.Turtle()
t.penup()
t.pencolor("black")
t.speed(50)

#first row
t.setpos(-200,-200)
for x in range(15):
    square("black")
square("blue")
square("black")
square("royal blue")
square("light steel blue")
square("navajo white")
for x in range(2):
    square("black")
square("gray")
square("blue")
for x in range(2):
    square("black")

#Second row    
t.setpos(-200, -220)
for x in range(16):
    square("black")
square("royal blue")
square("light steel blue")
square("navajo white")
square("peach puff")
for x in range(2):
    square("black")
