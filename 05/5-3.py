#3
import turtle
turtle.shape("turtle")
i = 20
for t in range(3,13):
    for y in range(t):
        turtle.forward(1+2*t)
        turtle.right(360/t)
