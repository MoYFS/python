import turtle
turtle.speed(0)
colors=["red","blue","green","yellow"]
turtle.hideturtle()
for i in range(100):
    turtle.pencolor(colors[i%4])
    turtle.circle(i)
    turtle.left(91)
turtle.done()