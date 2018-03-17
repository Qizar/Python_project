import turtle

turtle.bgcolor("red")

afzal = turtle.Turtle()


afzal.color("yellow")
afzal.speed(0)
afzal.shape("turtle")


def square():
    for i in range(4):
        afzal.forward(100)
        afzal.right(90)
        
for i in range(50):
    square()
    afzal.right(10)

