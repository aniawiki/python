import turtle 

i = 50

tu = turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("brown")

tu.left(90)
tu.backward(i)
tu.speed(200)


def tree(i):
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)
        tu.color("brown")

        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)


tree(i)
turtle.done()
