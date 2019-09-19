import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(5)

# draw curved arc
drawer.penup()
drawer.goto(0, -20)
drawer.pendown()
drawer.circle(100, 70)

# draw segmented arc
drawer.penup()
drawer.goto(0, 20)
drawer.pendown()
drawer.setheading(180)
drawer.circle(-100, -180, 7)

wn = trtl.Screen()
wn.mainloop()
