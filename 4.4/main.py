import turtle


# Dictionary for all the themes of colours that the user can choose from
themes = {
    "reds": ["#FF0000", "#FF6347", "#FF7F7F"],
    "greens": ["#006400", "#228B22", "#32CD32"],
    "blues": ["#0000FF", "#1E90FF", "#87CEFA"],
    "greys": ["#333333", "#666666", "#999999"],
    "rainbow": ["#FF0000", "#FFA500", "#FFDE21", "#80EF80", "#90D5FF", "#3C3CE8","#8F00FF"]
}

# Defining the rotating shapes function with the parameters t, length, turns, angle, colours, and i
def draw_rotating_shapes(t, length, turns, angle, colours, i=0):
    # Base case/ terminating case
    if turns == 0:
        return i

    # Cycles through the colours list without going out of range
    t.color(colours[i % len(colours)])
    t.width(6) 


    for e in range(3):
        t.forward(length)

        # Change how much it turns to create the shape based off of the shape that user inputted
        # Hexagon
        if shape == 2:
            t.left(60)
            t.width(4)
        # Square
        elif shape == 3:
            t.left(90)
            t.width(4)
        # Triangle
        elif shape == 4:
            t.left(120)
            t.width(4)
        # Star
        elif shape == 5:
            t.left(150)
            t.width(4)
        # Spiral
        else:
            t.left(30)
            t.width(4)

    # Rotate slightly and recurse
    t.right(angle)

    # The "length" and "turns" parameters change
    # Length increases by 2 to make each shape a bit larger than the last
    # Turns decreases by 1 to keep rotating until it reaches the base case
    return draw_rotating_shapes(t, length+2, turns - 1, angle, colours, i + 1)

# Keep asking the user if they do not select one of the options given
while True:
    # User input for the colour of the first set of rotating shapes
    theme = input("Colour Set 1: (reds, greens, blues, greys, rainbow)").strip("!.?,").lower()
    if theme in themes:
       break
    print("Please type a valid option")

while True: 
    # User input for the colour of the second set of rotating shapes
    theme2 = input("Colour Set 2: (reds, greens, blues, greys, rainbow)").strip("!.?,").lower()
    if theme2 in themes:
        break
    print("Please type a valid option")

# User input for which shape they wish to rotate around
shape = int(input("Enter the number of the shape you want to work with. Any other numbers inputted will result in the spiral being used:\n1) Spiral 2) Hexagon 3) Square 4) Triangle 5) Star"))

# Defining the turtle, its speed, the background colour of the screen, and hiding it
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
background = turtle.Screen()
background.bgcolor("black")

# The number of turns the shape does
turns = 60
# The angle that each shape turns to go around a full circle
angle = 360 / turns

# The side length of each side of the shape
length = 4

# Capture recursion count for the first draw
numRecursions1 = draw_rotating_shapes(t, length, turns, angle, themes[theme])

# Move the turtle to the middle to set up for the second draw
t.penup()
t.goto(0, 0)
t.pendown()

# Capture recursion count for the second draw
numRecursions2 = draw_rotating_shapes(t, length, turns-30, angle, themes[theme2])

# Print results
print("Recursive calls made for the first layer: " +str(numRecursions1))
print("Recursive calls made for the second layer: " + str(numRecursions2))
print("Total recurisve calls: " + str(numRecursions1 + numRecursions2))

turtle.done()