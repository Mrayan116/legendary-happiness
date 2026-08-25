import turtle

def square(clr):#
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
t.speed(0)


#first row.
t.goto(-100,-100)
for x in range(2):
    square("black")

#second row
t.goto(-100,-80)
for x in range(1):
    square("black")
square("red")
square("black")

#third row
t.goto(-80,-60)
for x in range(3):
    square("black")

#fourth row
t.goto(-60,-40)
for x in range(3):
    square("black")

#fifth row
t.goto(-40,-20)
for x in range(3):
    square("black")
t.goto(120,-20)
for x in range(3):
    square("black")

#sixth row
t.goto(-20,0)
for x in range(3):
    square("black")
t.goto(80,0)
square("black")
square("black")
for x in range(2):
    square("grey20")
for x in range(2):
    square("black")

#seventh row
t.goto(0,20)
for x in range(5):
    square("black")
for x in range(1):
    square("grey20")
for x in range(2):
    square("black")
t.goto(180,20)
square("black")

#eight row
t.goto(20,40)
square("black")
square("firebrick3")
square("firebrick4")
square("grey20")
square("black")
square("black")

#ninth row
t.goto(20,60)
square("black")
square("firebrick1")
square("firebrick")
square("black")
square("black")
square("firebrick")
square("firebrick4")

#tenth row
t.goto(0,80)
square("black")
square("black")
square("grey20")
square("black")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#eleventh row
t.goto(0,100)
square("black")
square("grey20")
square("black")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#12th row
t.goto(-20,120)
square("grey20")
square("grey20")
square("black")
square("black")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#13
t.goto(-20,140)
square("grey10")
square("grey20")
square("black")
t.goto(60,140)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#14
t.goto(-20,160)
square("grey10")
square("grey20")
t.goto(80,160)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#15
t.goto(0,180)
square("grey10")
square("grey20")
t.goto(100,180)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#16
t.goto(120,200)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#17
t.goto(140,220)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#18
t.goto(160,240)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#19
t.goto(180,260)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#20
t.goto(200,280)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("grey20")
square("firebrick")
square("firebrick4")

#21
t.goto(220,300)
square("firebrick")
square("firebrick1")
square("black")
square("grey20")
square("black")
square("firebrick")
square("firebrick4")

#21
t.goto(240,320)
square("firebrick")
for x in range(3):
    square("firebrick1")
square("firebrick3")
square("firebrick4")

#22
t.goto(260,340)
for x in range(5):
    square("firebrick4")


t.goto(-200, 300)
t.pendown()
t.circle(20)
