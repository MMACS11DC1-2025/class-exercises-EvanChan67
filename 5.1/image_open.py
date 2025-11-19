from PIL import Image

def is_colour(r, g, b):
    if 0 <= r < 25 and 230 < g <= 255 and 0 <= b < 25:
        return "green"
    elif 230 < r <=255 and 0 <= g < 25 and 0 <= b < 25:
        return "red"
    return "blue"
    
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

pixel = image_green[0, 0]

r = pixel[0]
g = pixel[1]
b = pixel[2]

print(is_colour(r, g, b))
