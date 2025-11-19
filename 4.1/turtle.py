import turtle

pulse = turtle.Turtle()
screen = turtle.Screen()
pulse.speed(6)

def wave(x, y):
    pulse.penup()
    pulse.goto(x - (screen.window_width() / 2), y)
    pulse.pendown()

    amplitude = float(input("Enter the height of the wave: "))


    wavelength = 100
    right_edge = screen.window_width() / 2

    while pulse.xcor() < right_edge:
        pulse.left(45)
        pulse.forward(amplitude)
        pulse.right(90)
        pulse.forward(amplitude)
        pulse.left(45)

wave(0, 0)