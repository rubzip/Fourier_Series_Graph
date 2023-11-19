import tkinter as tk
import turtle
import os


screen = turtle.Screen()
t = turtle.Turtle("turtle")
t.speed = 0 # Here I'm setting the speed at the maximum
t.width(4)
path = list()


def yes_or_no_window(title, question):
    root = tk.Tk()
    root.title(title)

    def yes():
        root.resultado = "Yes"
        root.destroy()

    def no():
        root.resultado = "No"
        root.destroy()

    label = tk.Label(root, text=question)
    label.pack(padx=20, pady=10)

    yes_button = tk.Button(root, text="Yes", command=yes)
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(root, text="No", command=no)
    no_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()

    return root.resultado


def emergent_window_question(window_name, question, valid_values=("y", "n", "")):
    awnser = screen.textinput(window_name, question)
    while awnser.lower()[0] not in valid_values:
        awnser = screen.textinput(window_name, question)
    
    return awnser.lower()[0]


def get_filename():
    filename = screen.textinput("Get filename", "Please enter the file name:")
    want_to_overwrite = "n"
    if filename is None:
        return ""
    
    while os.path.exists(filename) and want_to_overwrite=="No":
        want_to_overwrite = yes_or_no_window("WARNING", f"{filename} already exists, are you sure about overwriting it?")
        if want_to_overwrite=="No":
            filename = get_filename()
    
    return filename


def dragging(x, y):
    global path
    global t
    path.append((x, y))

    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def remove_path(x=0, y=0):
    global path
    global t

    if len(path)>1:
        decision = yes_or_no_window("Clear drawing", "Are you about deleting your current drawing?")
        print(decision)
        if decision=="Yes":
            t.clear()
            path = list()


def increaseLineWidth():
    global t
    t.width(t.width() + 1)


def decreaseLineWidth():
    global t
    if t.width() > 1:
        t.width(t.width() - 1)


def go_reverse():
    pass


def saveDrawing():
    global path
    filename = get_filename()
    with open(filename, "w") as f:
        for x, y in path:
            print(x, y)
            f.write(f"{x}\t{y}\n")


def closeWindow():
    global screen
    want_to_close = yes_or_no_window("WARNING", "Do you want to close the program?")=="Yes"
    if want_to_close:
        want_to_save = yes_or_no_window("WARNING", "Do you want to close without saving your draw?")=="No"
        if want_to_save:
            saveDrawing()
        screen.bye()