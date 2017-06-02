from Tkinter import *


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
