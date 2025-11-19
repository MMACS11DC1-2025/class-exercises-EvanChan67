from PIL import Image

image_og = Image.open("5.4/jelly_beans.jpg")
pixels = image_og.load()

image_output = Image.open("5.4/jelly_beans.jpg")
w = image_og.width
h = image_og.height

for x in range(w):
    for y in range(h):
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]

        if r > 160 and g > 160 and b < 50:
            white_colour = 255
            new_colour = (white_colour, white_colour, white_colour)
            image_output.putpixel((x, y), new_colour)

image_output.save("output.png", "png")