from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno

import tkinter as tk

class drawer:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.speed = 0  # I'm setting the speed at the maximum
        self.width = 4  # I'm setting the width to default
        self.path = []  # Here I'm storing the drawing path
        self.drawn_lines = []

        self.x = 150
        self.y = 100
        self.R = 5
        
        self.cursor_id = self.canvas.create_oval(self.x-self.R, self.y-self.R, self.x+self.R, self.y+self.R, fill='red')

    def run(self):
        self.canvas.tag_bind(self.cursor_id, '<ButtonPress-1>', self.on_drag_start)
        self.canvas.tag_bind(self.cursor_id, '<B1-Motion>', self.on_dragging)

        self.canvas.bind('<Button-3>', self.remove_path)
        self.canvas.bind('<Button-1>', self.move_cursor)

        self.root.bind(
            "s", self.save_drawing
        )  # Press 's' key for saving the path
        self.root.bind(
            "x", self.close_window
        )  # Press 'x' key to close window
        self.root.bind(
            "z", self.undo_movement
        )  # Press 'x' key to close window
        self.root.bind(
            "<Up>", self.increase_line_width
        )  # Press 'Up' arrow key to increase line width
        self.root.bind(
            "<Down>", self.decrease_line_width
        )  # Press 'Down' arrow key to increase line width
        
        self.root.mainloop()
    
    def actualize_pos(self, event):
        self.x = event.x
        self.y = event.y
    
    def calculate_delta(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y

        return delta_x, delta_y

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
    
    def undo_movement(self, a=None, b=None):
        if len(self.path) > 0:
            last_line_id = self.drawn_lines.pop()
            self.canvas.delete(last_line_id)
            self.path.pop()
            if len(self.path) > 0:
                x, y = self.path[-1]
                delta_x, delta_y = x - self.x, y - self.y
                self.canvas.move(self.cursor_id, delta_x, delta_y)
                self.x, self.y = x, y    
        
    def move_cursor(self, event):
        if len(self.path) == 0:
            delta_x, delta_y = self.calculate_delta(event)
            
            self.canvas.move(self.cursor_id, delta_x, delta_y)
            
            self.actualize_pos(event)

    def remove_path(self, event):
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
    
    def increase_line_width(self, a=None, b=None):
        self.width += 1

    def decrease_line_width(self, a=None, b=None):
        self.width = max(self.width-1, 1)

    def save_drawing(self, a=None, b=None):
        if len(self.path) > 0:
            filename = asksaveasfilename()
            with open(filename, "w") as f:
                for x, y in self.path:
                    f.write(f"{x}\t{y}\n")
    
    def close_window(self, a=None, b=None):
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





a = drawer()
a.run()