###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)




rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

tim.penup()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    

    if dot_counts%10 == 0 :
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen
