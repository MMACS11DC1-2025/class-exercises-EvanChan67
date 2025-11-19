from PIL import Image


image_source = Image.open("5.1/beach.jpg")
pixels = image_source.load()


image_output = Image.open("5.1/beach.jpg")
width = image_output.width
height = image_output.height


for i in range(width):
    for j in range(height):
        r = pixels[i, j][0]
        g = pixels[i, j][1]
        b = pixels[i, j][2]
        grey_value = (r + g + b) // 3
        new_colour = (grey_value, grey_value, grey_value)

        image_output.putpixel((i, j), new_colour)

image_output.save("output.png", "png")