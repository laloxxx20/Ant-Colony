
# from Tkinter import *

# master = Tk()

# w = Canvas(master, width=200, height=100)
# w.pack()

# # w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")

# mainloop()

from Tkinter import *

# canvas_width = 500
# canvas_height = 150


# def paint(event):
#     python_green = "white"
#     x1, y1 = (event.x - 1), (event.y - 1)
#     x2, y2 = (event.x + 1), (event.y + 1)
#     w.create_oval(x1, y1, x2, y2, fill=python_green)


# master = Tk()
# master.title("Points")
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height,
#            bg="black")
# w.pack(expand=YES, fill=BOTH)
# w.bind("<B1-Motion>", paint)

# message = Label(master, text="Press and Drag the mouse to draw")
# message.pack(side=BOTTOM)

# mainloop()


class Draw(object):
    window_title = "Ants Colony"
    window_height = 600
    window_width = 600
    window_bg = "black"
    point_color = "white"
    point_radio = 10
    line_color = "white"
    line_thickness = 2
    window = Tk()
    canvas = None

    def __init__(self, *args, **kargs):
        self.window.title(self.window_title)
        self.canvas = Canvas(
            self.window, width=self.window_width,
            height=self.window_height, bg=self.window_bg)
        self.canvas.pack()

    def draw_point(self, x, y):
        x1, y1 = (x - self.point_radio), (y - self.point_radio)
        x2, y2 = (x + self.point_radio), (y + self.point_radio)
        return self.canvas.create_oval(x1, y1, x2, y2, fill=self.point_color)

    def delete_point(self, point):
        self.canvas.delete(point)

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(
            x1, y1, x2, y2,
            fill=self.line_color, width=self.line_thickness)

    def changecolor_point(self, color):
        self.point_color = color

    def changecolor_radio(self, radio):
        self.point_radio = radio

    def __del__(self):
        self.window.mainloop()
