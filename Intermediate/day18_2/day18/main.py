###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('Python\Python_WorkSpace\Intermediate\day18_2\image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)