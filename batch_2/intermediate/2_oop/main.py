# import turtle
# timmy = turtle.Turtle()

# def define_turtle():
#     timmy.shape("turtle")
#     timmy.color("red")
#     return timmy
# define_turtle()

# timmyTurtle = define_turtle()
# timmyTurtle.fd(100)
# timmyTurtle.right(90)
# timmyTurtle.fd(100)
# timmyTurtle.right(90)
# timmyTurtle.fd(100)
# timmyTurtle.right(90)
# timmyTurtle.fd(100)


# my_screen = turtle.Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
# python -v
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
print(table)