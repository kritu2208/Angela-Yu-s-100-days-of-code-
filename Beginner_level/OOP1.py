# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red" , "green")
# timmy.forward(200)

# print(timmy)

# my_screen = Screen()

# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name" , "Type"]
table.add_row (["Pikachu","Electric"])
table.add_row (["Squirtle","Water"]) 
table.add_row (["Charmander","Fire"]) 

table.align = "c"

print(table)

