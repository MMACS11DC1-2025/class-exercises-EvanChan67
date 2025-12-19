import time
t0 = time.time()
from PIL import Image

t1 = time.time()

file = Image.open("5.4/jelly_beans.jpg")
jbimg = file.load()

width = file.width
height = file.height
yellow_pixels = 0

t2 = time.time()

for i in range(width):
    for j in range(height):

        r = jbimg[i, j][0]
        g = jbimg[i, j][1]
        b = jbimg[i, j][2]

        if r > 150 and g > 150 and b < 100:
            yellow_pixels +=1

t3 = time.time()

print(yellow_pixels)
print(width*height)

percent_yellow = 100*yellow_pixels/(width*height)
report = "There are {:.3f} percent yellow jellybeans.".format(percent_yellow)
print(report)

module_load = t1 - t0
image_open_load = t2- t1
loop = t3-t2
entire = t3-t0

timings = "It took {:.2f}s to import PIL, {:.2f}s to load the image, and {:.2f}s tp dp the loop. All in all it took {:.2f}s".format(module_load, image_open_load, loop, entire)
print(timings)