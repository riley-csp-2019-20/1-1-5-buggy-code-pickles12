#   a115_buggy_image.py
import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)

w = 6
y = 70
z = 360 / w
drawer.pensize(5)
n = 0
while (n < w):
  drawer.goto(0,0)
  drawer.setheading(z*n)
  drawer.forward(y)
  n = n + 1
drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()