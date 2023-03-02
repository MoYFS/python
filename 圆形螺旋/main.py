import turtle
turtle.setup(840,840)
turtle.speed(0)
colors=["red","blue","green","yellow"]
turtle.hideturtle()
for i in range(200):
    turtle.pencolor(colors[i%4])
    turtle.circle(200-i)
    turtle.left(91)
turtle.done()