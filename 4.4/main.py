import turtle

# --- color themes dictionary ---
themes = {
    "reds": ["#FF0000", "#FF6347", "#FF7F7F"],
    "greens": ["#006400", "#228B22", "#32CD32"],
    "blues": ["#0000FF", "#1E90FF", "#87CEFA"],
    "shades": ["#333333", "#666666", "#999999"]
}

def draw_rotating_triangles(t, length, turns, angle, colors, i=0):
    if turns == 0:
        return

    t.color(colors[i % len(colors)])
    t.width(2) 

    # draw one triangle
    for _ in range(3):
        t.forward(length)
        t.left(120)

    # rotate slightly and recurse
    t.right(angle)
    draw_rotating_triangles(t, length+2, turns - 1, angle, colors, i + 1)



theme = input("Colour Set 1: ").strip().lower()
if theme not in themes:
    theme = "reds"
theme2 = input("Colour Set 2: ").strip().lower()
if theme2 not in themes:
    theme2 = "blues"
length = int(input("Enter triangle side length (e.g. 100): "))

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


turns = 60
angle = 360 / turns

# draw outer circle of triangles
draw_rotating_triangles(t, length, turns, angle, themes[theme])

# move inward slightly for the smaller inner set
t.penup()
t.goto(0, 0)
t.pendown()

# draw inner circle of smaller triangles
draw_rotating_triangles(t, length/2 , turns, angle, themes[theme2])