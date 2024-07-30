from turtle import Turtle, Screen


# function
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_up():
    tim.left(10)


tim = Turtle()
screen = Screen()


screen.listen()
screen.onkey(key="d",fun=move_forward)
screen.exitonclick()



