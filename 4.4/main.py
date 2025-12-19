# Evan Chan
# Rotating Shapes Program

import turtle
import random
# Dictionary for all the themes of colours that the user can choose from
themes = {
    "reds": ["#FF0000", "#FF6347", "#FF7F7F"],
    "greens": ["#006400", "#228B22", "#32CD32"],
    "blues": ["#0000FF", "#1E90FF", "#87CEFA"],
    "greys": ["#333333", "#666666", "#999999"],
    "rainbow": ["#FF0000", "#FFA500", "#FFDE21", "#80EF80", "#90D5FF", "#3C3CE8","#8F00FF"]
}

# Defining the rotating shapes function with the parameters t, length, turns, angle, colours, levels, and colour index
def draw_rotating_shapes(t, length, turns, angle, colours, levels, colour_index = 0):
    # Base case/ terminating case
    if turns == 0:
        return 0

    # Setting the colour of the line(s)
    t.color(colours[colour_index])

    for i in range(levels):
        t.forward(length)

        # Change how much it turns to create the shape based off of the shape that user inputted
        # Octagon
        if shape == 1:
            t.left(45)
        # Hexagon
        if shape == 2:
            t.left(60)
        # Square
        elif shape == 3:
            t.left(90)
        # Triangle
        elif shape == 4:
            t.left(120)
        # Star
        elif shape == 5:
            t.left(150)

    # Rotate slightly
    t.right(angle)
    
    # Cycle through a new colour from the colour list
    next_colour_index = colour_index + 1
    if next_colour_index == len(colours):
        # If the next index is out of the range reset it back to 0 (the start of the list)
        next_colour_index = 0
        
    # The "length" and "turns" parameters change
    # Length increases by 2 to make each shape a bit larger than the last
    # Turns decreases by 1 to keep rotating until it reaches the base case
    # Returns the function increased by 1 to count the number of calls
    return draw_rotating_shapes(t, length+2, turns - 1, angle, colours, levels, next_colour_index) + 1

def draw_stars(t, n):

    # Base case/ terminating case
    if n == 0: 
      return 0
    
    t.penup()
    # Have the turtle move to a random point on the screen
    t.goto(random.randint(-300,300), random.randint(-300,300))

    # Draw a white  dot at that location, with random size between 2 and 10
    t.dot(random.randint(2,10), "white")

    # n decreases by 1 to move it closer to the base case and to signify one less dot that needs to be drawn
    return draw_stars(t, n-1) + 1
    

# While loops used to make sure the user provides a valid input that wont crash the program

while True:
  # User input for which shape they wish to rotate around
  shape = int(input("Enter an integer of the shape you want to rotate:\n1) Octagon 2) Hexagon 3) Square 4) Triangle 5) Star"))
  if 1<= shape <=5:
    break
  print("Invalid option. Please type an integer from 1-5")
  
while True:
  # User input for the amount of levels they want for the final drawing
  levels = int(input("Enter an integer for the amount of levels (1-5): Higher = more dense"))
  if 1<= levels <=5:
    break
  print("Invalid option. Please type an integer from 1-5")
  
while True:
    # User input for the colour of the first set of rotating shapes
    theme = input("Enter the theme for the outer layer: (reds, greens, blues, greys, rainbow)").strip("!.?, ").lower()
    if theme in themes:
       break
    print("Please type a valid colour")

while True: 
    # User input for the colour of the second set of rotating shapes
    theme2 = input("Enter the theme for the inner layer: (reds, greens, blues, greys, rainbow)").strip("!.?, ").lower()
    if theme2 in themes:
        break
    print("Please type a valid colour")
    
while True:
  # User input for number of stars
  numStars = int(input("Enter the number of stars you want (1-50)"))
  if 1<= numStars <=50:
    break
  print("Invalid option. Type a number from 1-50")

# Defining the turtle, its speed, the background colour of the screen, and hiding it
t = turtle.Turtle()
t.width(4)
t.speed(0)
t.hideturtle()
background = turtle.Screen()
background.bgcolor("black")

# The number of turns the shape does
turns = 90
# The angle that each shape turns to go around a full circle
angle = 360 / turns

# The side length of each side of the shape
length = 4

# Capture recursion count for the first draw
numRecursions1 = draw_rotating_shapes(t, length, turns, angle, themes[theme], levels)

# Move the turtle to the middle to set up for the second draw
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

# Capture recursion count for the second draw
numRecursions2 = draw_rotating_shapes(t, length, turns-30, angle, themes[theme2], levels)

# Capture recursion count for the stars
numRecursions3 = draw_stars(t, numStars)

# Print results
print("Recursive calls made for the first layer: " +str(numRecursions1))
print("Recursive calls made for the second layer: " + str(numRecursions2))
print("Recursive calls made for the third layer: " + str(numRecursions3))
print("Total recursive calls: " + str(numRecursions1 + numRecursions2 + numRecursions3))

# End the program
turtle.done()