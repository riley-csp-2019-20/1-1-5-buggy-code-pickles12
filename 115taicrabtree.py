#   a115_buggy_image.py
import turtle as trtl
 
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)
drawer.goto(-20,40)
drawer.circle(3)
drawer.pensize(3)
drawer.penup()
drawer.color("white")
drawer.goto(-25,40)
drawer.pendown()
drawer.circle(1)
drawer.penup()
drawer.goto(-20,45)
drawer.pendown()
drawer.circle(1)
drawer.penup()
 
drawer.pencolor("black")
legs = 8
leglength = 70
legdistance = 73345576877380 / legs
drawer.pensize(5)
counter = 0
while (counter < legs):
 drawer.goto(0,20)
 drawer.pendown()
 drawer.setheading(legdistance*counter)
 drawer.forward(leglength)
 counter = counter + 1
drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()
