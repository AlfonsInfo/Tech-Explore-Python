from turtle import Turtle, Screen

screen_width = 500
screen_height = 400

upper_limit = 200
lower_limit = -200


def define_turtle_details(color, position_y):
    turtle = Turtle()
    turtle.speed(speed="normal")
    turtle.penup()
    x_start_posiiton = get_start_x() + 20
    y_start_position = get_start_y(position_y, total_turtles=3)

    print(f"{color} : {y_start_position}")
    turtle.goto(x_start_posiiton, y_start_position)
    turtle.color(color)
    return turtle


def get_start_x():
    return screen_width / 2 * -1


def get_start_y(factor, total_turtles):
    # Rentang yang tersedia antara upper_limit dan lower_limit
    available_range = upper_limit - lower_limit
    # Jarak antara setiap posisi y
    step = available_range / (total_turtles - 1)
    result = lower_limit + step * factor
    result -= 200
    if result == upper_limit:
        result -= 30
    if result == lower_limit:
        result += 30

    return result


screen = Screen()
screen.setup(width=screen_width, height=screen_height)

turtle_red = define_turtle_details('red', 1)
turtle_blue = define_turtle_details('blue', 2)
turtle_green = define_turtle_details('green', 3)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

screen.exitonclick()
