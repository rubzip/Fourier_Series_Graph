import turtle


def drawer(filename: str):
    screen = turtle.Screen()
    screen.title(f"Generating: {filename}")
    t = turtle.Turtle()
    
    dots = []
    