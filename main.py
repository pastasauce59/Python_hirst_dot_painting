# import colorgram

# colors = colorgram.extract('image.jpeg', 6)

# list_of_colors = []
# for color in colors:
#     rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
#     list_of_colors.append(rgb)

# print(list_of_colors)

color_list = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33)]

import random
import turtle as t
painter = t.Turtle()
t.colormode(255)

def hirst_paint():
    painter.penup()
    painter.speed('fastest')
    yaxis = -250
    while yaxis <= 200:
        painter.setx(-250)
        painter.sety(yaxis)
        for paints in range(10):
            painter.color(random.choice(color_list))
            painter.dot(20)
            painter.forward(50)
        
        yaxis += 50

    painter.hideturtle()   

hirst_paint()


screen = t.Screen()
screen.exitonclick()