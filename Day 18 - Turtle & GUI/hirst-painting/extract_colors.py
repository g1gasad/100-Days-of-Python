import colorgram

colors = colorgram.extract('image.jpg', 30)

image_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    image_colors.append(rgb_tuple)
