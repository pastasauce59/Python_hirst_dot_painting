import colorgram

colors = colorgram.extract('image.jpeg', 6)
# print(colors[0].rgb[0])

list_of_colors = []
for color in colors:
    rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
    list_of_colors.append(rgb)

print(list_of_colors)