import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main(num):
    turtle.setup(800,600)
    turtle.penup()
    turtle.goto(-300,200)
    turtle.pendown()
    turtle.pensize(2)
    for i in range(num):
        koch(400,num)
        turtle.right(360/num)
    turtle.hideturtle()

main(4)
