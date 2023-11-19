from fun import *

def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    
    turtle.onscreenclick(remove_path, 3)            # When right mouse button is clicked the drawing is deleted
    screen.onkeypress(saveDrawing, "s")             # Press 's' key for saving the path
    screen.onkeypress(increaseLineWidth, "Up")      # Press 'Up' arrow key to increase line width
    screen.onkeypress(decreaseLineWidth, "Down")    # Press 'Down' arrow key to decrease line width
    screen.onkeypress(closeWindow, "x")             # Press 'x' key for closing the window

    screen.mainloop()  

main()