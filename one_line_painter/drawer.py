import turtle

from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno

from time import sleep

class Drawer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.t = turtle.Turtle("turtle")  # Creating the drawing turtle
        self.t.speed = 0  # I'm setting the speed at the maximum
        self.t.width(4)  # I'm setting the width to default
        self.path = []  # Here I'm storing the drawing path

    def run(self):
        turtle.listen()
        self.t.ondrag(drawer.dragging)  # When we drag the turtle object call dragging

        turtle.onscreenclick(self.remove_path, 3)
        turtle.onscreenclick(self.move_turtle, 1)
        self.screen.onkeypress(
            self.save_drawing, "s"
        )  # Press 's' key for saving the path
        self.screen.onkeypress(
            self.close_window, "x"
        )  # Press 'x' key to close window
        self.screen.onkeypress(
            self.increase_line_width, "Up"
        )  # Press 'Up' arrow key to increase line width
        self.screen.onkeypress(
            self.decrease_line_width, "Down"
        )  # Press 'Down' arrow key to increase line width
        self.screen.onkeypress(self.undo_last, "z")

        self.screen.mainloop()

    def dragging(self, x, y):
        self.t.ondrag(None)
        self.t.setheading(self.t.towards(x, y))
        self.t.goto(x, y)
        self.t.ondrag(self.dragging)

        self.path.append((x, y))

    def move_turtle(self, x, y):
        if len(self.path) == 0:
            self.t.penup()
            self.t.goto(x, y)
            self.t.pendown()

    def remove_path(self, x=0, y=0):
        if len(self.path) > 0:
            # decision = emergent_window_question("Clear drawing", "Are you about deleting your current drawing? (yes/no)")
            want_to_delete = askyesno(
                "Clear drawing", "Are you about deleting your current drawing?"
            )
            if want_to_delete:
                self.t.clear()
                self.path = []

    def undo_last(self):
        if len(self.path) > 0:
            self.t.undo()
            self.path.pop()
            sleep(0.3)

    def increase_line_width(self):
        self.t.width(self.t.width() + 1)

    def decrease_line_width(self):
        if self.t.width() > 1:
            self.t.width(self.t.width() - 1)

    def save_drawing(self):
        if len(self.path) > 0:
            filename = asksaveasfilename()
            with open(filename, "w") as f:
                for x, y in self.path:
                    f.write(f"{x}\t{y}\n")

    def close_window(self):
        if len(self.path) > 0:
            want_to_close = askyesno("WARNING", "Are you sure to close the program?")
            if want_to_close:
                want_to_save = askyesno(
                    "Do you want to save?", "Do you want to save the drawing before closing?"
                )
                if want_to_save:
                    self.save_drawing()
                self.screen.bye()
        else:
            self.screen.bye()


if __name__ == "__main__":
    drawer = Drawer()
    drawer.run()
