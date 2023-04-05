import turtle
turtle.setup(840,720)
turtle.fillcolor("red")
turtle.speed(0)
turtle.penup()
turtle.goto(-135,50)
turtle.pendown()
turtle.begin_fill()
#turtle.pencolor("red")
# for i in range(5):
#     turtle.forward(300)
#     turtle.right(144)
turtle.pencolor("black")
for i in range(12):
    turtle.forward(300)
    turtle.right(150)
turtle.end_fill()
turtle.hideturtle()
turtle.done()