import turtle
import os

screen = turtle.Screen()
t = turtle.Turtle("turtle")
t.speed = 0 # Here I'm setting the speed at the maximum
t.width(4)
path = list()


def emergent_window_question(window_name, question, valid_values=("y", "n")):
    confirm_clear = screen.textinput(window_name, question)
    while confirm_clear.lower()[0] not in valid_values:
        confirm_clear = screen.textinput(window_name, question)
    
    return confirm_clear.lower()[0]


def get_filename():
    filename = screen.textinput("Get filename", "Please enter the file name:")
    want_to_overwrite = "n"
    while os.path.exists(filename) and want_to_overwrite=="n":
        want_to_overwrite = emergent_window_question("WARNING", f"{filename} already exists, are you sure about overwriting it? (yes/no)")
        if want_to_overwrite=="n":
            filename = get_filename()
    print(os.listdir())
    return filename


def dragging(x, y):
    global path
    path.append((x, y))

    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def remove_path(x=0, y=0):
    global path
    if len(path)>1:
        decision = emergent_window_question("Clear drawing", "Are you about deleting your current drawing? (yes/no)")
        if decision=="y":
            t.clear()
            path = list()


def increaseLineWidth():
    t.width(t.width() + 1)
    print(t.speed)


def decreaseLineWidth():
    if t.width() > 1:
        t.width(t.width() - 1)


def saveDrawing():
    global path
    filename = get_filename()
    with open(filename, "w") as f:
        for x, y in path:
            print(x, y)
            f.write(f"{x}\t{y}\n")

def closeWindow():
    global screen
    if emergent_window_question("WARNING", "Do you want to close the program? (yes/n)")=="y":
        if emergent_window_question("WARNING", "Do you want to close without saving your draw? (yes/n)")=="n":
            saveDrawing()
        screen.bye()



def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(remove_path, 3)

    screen.onkeypress(saveDrawing, "s")             # Press 's' key for saving the path
    screen.onkeypress(increaseLineWidth, "Up")      # Press 'Up' arrow key to increase line width
    screen.onkeypress(decreaseLineWidth, "Down")    # Press 'Down' arrow key to increase line width
    screen.onkeypress(closeWindow, "x")

    screen.mainloop()  

main()