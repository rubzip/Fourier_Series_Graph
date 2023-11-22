from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno

import tkinter as tk

class Drawer:
    def __init__(self):
        # Constants for canvas dimensions, padding, and cursor radius
        self.WIDTH = 600
        self.HEIGHT = 600
        self.PADDING = 10
        self.R = 5

        self.help_path = "./help.info"

        # Initialize the Tkinter app and canvas
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()

        # Initialize variables for drawing properties and coordinates
        self.width = 1  # Default line width
        self.path = []  # Store drawing path
        self.drawn_lines = []  # Store drawn lines on canvas

        # Initial cursor position
        self.initial_x = 150
        self.initial_y = 100
        self.x = self.initial_x
        self.y = self.initial_y
        
        # Create the cursor on canvas
        self.cursor_id = self.canvas.create_oval(self.x-self.R, self.y-self.R, self.x+self.R, self.y+self.R, fill='red')
        self.closing_line_id = None

    def run(self): # main loop method
        self.canvas.tag_bind(self.cursor_id, '<ButtonPress-1>', self.on_drag_start)
        self.canvas.tag_bind(self.cursor_id, '<B1-Motion>', self.on_dragging)

        self.canvas.bind('<Button-1>', self.change_initial_pos)  # Left click changes the initial position
        self.canvas.bind('<Button-3>', self.delete_drawing)  # Right click deletes the current drawing
        
        self.root.bind("s", self.save_drawing)  # Press 's' key for saving the path
        self.root.bind("x", self.close_window)  # Press 'x' key to close window
        self.root.bind("z", self.undo_movement)  # Press 'z' key to undo the last movement
        self.root.bind("h", self.show_help)  # Press 'h' key to read documentation
        self.root.bind("<Up>", self.increase_line_width)  # Press 'Up' arrow key to increase line width
        self.root.bind("<Down>", self.decrease_line_width)  # Press 'Down' arrow key to increase line width
        
        self.root.mainloop()
    
    def actualize_pos(self, event):
        self.x = max(self.PADDING, min(self.WIDTH-self.PADDING, event.x))
        self.y = max(self.PADDING, min(self.HEIGHT-self.PADDING, event.y))
    
    def calculate_delta(self, event):
        delta_x = max(self.PADDING, min(self.WIDTH-self.PADDING, event.x)) - self.x
        delta_y = max(self.PADDING, min(self.HEIGHT-self.PADDING, event.y)) - self.y

        return delta_x, delta_y
    
    def actualize_closing_line(self):
        if self.closing_line_id is not None:
            self.canvas.delete(self.closing_line_id)
        self.closing_line_id = self.canvas.create_line(self.x, self.y, self.initial_x, self.initial_y, fill='black', width=self.width)

    def on_drag_start(self, event):
        # Capture the starting position of the oval when dragging starts
        latest_line = self.canvas.create_line(self.x, self.y, event.x, event.y, fill='black', width=self.width)

        self.path.append((event.x, event.y))
        self.drawn_lines.append(latest_line)
        self.actualize_pos(event)
    
    def on_dragging(self, event):
        # Calculate the distance moved by the mouse and update the oval's position
        delta_x, delta_y = self.calculate_delta(event)

        self.canvas.move(self.cursor_id, delta_x, delta_y)
        latest_line = self.canvas.create_line(self.x, self.y, event.x, event.y, fill='black', width=self.width)

        self.path.append((event.x, event.y))
        self.drawn_lines.append(latest_line)

        self.actualize_pos(event)
        self.actualize_closing_line()
    
    def undo_movement(self, *args, **kwargs):
        # This method undo the last movement
        if len(self.path) > 0:
            last_line_id = self.drawn_lines.pop()
            self.canvas.delete(last_line_id)
            self.path.pop()
            if len(self.path) > 0:
                x, y = self.path[-1]
                delta_x, delta_y = x - self.x, y - self.y
                self.canvas.move(self.cursor_id, delta_x, delta_y)
                self.x, self.y = x, y
                
            self.actualize_closing_line()

    def change_initial_pos(self, event):
        # If the user haven't started drawing it's possible to move cursor
        if len(self.path) == 0:
            delta_x, delta_y = self.calculate_delta(event)
            
            self.canvas.move(self.cursor_id, delta_x, delta_y)
            
            self.actualize_pos(event)
            
            self.initial_x = self.x 
            self.initial_y = self.y

    def delete_drawing(self, event):
        if len(self.path) > 0:
            # decision = emergent_window_question("Clear drawing", "Are you about deleting your current drawing? (yes/no)")
            want_to_delete = askyesno(
                "Clear drawing", "Are you about deleting your current drawing?"
            )
            if want_to_delete:
                while self.drawn_lines:
                    last_line_id = self.drawn_lines.pop()
                    self.canvas.delete(last_line_id)
                self.path = []
                self.initial_x = self.x 
                self.initial_y = self.y
                
                if self.closing_line_id is not None:
                    self.canvas.delete(self.closing_line_id)
                    self.closing_line_id = None
    
    def increase_line_width(self, *args, **kwargs):
        self.width += 1

    def decrease_line_width(self, *args, **kwargs):
        self.width = max(self.width-1, 1)

    def save_drawing(self, *args, **kwargs):
        if len(self.path) > 0:
            filename = asksaveasfilename()
            with open(filename, "w") as f:
                f.write("x\ty\n")
                for x, y in self.path:
                    f.write(f"{x}\t{y}\n")
    
    def close_window(self, *args, **kwargs):
        if len(self.path) > 0:
            want_to_close = askyesno("WARNING", "Are you sure to close the program?")
            if want_to_close:
                want_to_save = askyesno(
                    "Do you want to save?", "Do you want to save the drawing before closing?"
                )
                if want_to_save:
                    self.save_drawing()
                self.root.destroy()
        else:
            self.root.destroy()
    
    def show_help(self, *args, **kwargs):
        with open(self.help_path, 'r') as f:
            help_dialog = f.read()

            help_window = tk.Toplevel(self.root)
            help_window.title("Help")
            
            label = tk.Label(help_window, text=help_dialog, padx=20, pady=20)
            label.pack()

if __name__=="__main__":
    drawer = Drawer()
    drawer.run()