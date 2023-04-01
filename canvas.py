import tkinter as tk

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint App")
        self.color = "black"
        
        # create canvas
        self.canvas = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # create clear button
        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()
        
        # create color buttons
        self.red_button = tk.Button(self.master, text="Red", bg="red", command=lambda: self.set_color("red"))
        self.red_button.pack(side=tk.LEFT)
        self.blue_button = tk.Button(self.master, text="Blue", bg="blue", command=lambda: self.set_color("blue"))
        self.blue_button.pack(side=tk.LEFT)
        self.green_button = tk.Button(self.master, text="Green", bg="green", command=lambda: self.set_color("green"))
        self.green_button.pack(side=tk.LEFT)
        
    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
    
    def clear_canvas(self):
        self.canvas.delete("all")
    
    def set_color(self, color):
        self.color = color

root = tk.Tk()
app = PaintApp(root)
root.mainloop()