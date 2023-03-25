import colorgram

colors = colorgram.extract('Python\Python_WorkSpace\Intermediate\day18\shi.jpg', 6)
first_color = colors[0]
rgb = first_color.rgb

red = rgb[0]

print(red)
