from tkinter import *

h = 500 # Height of window
w = 600 # Width of window

root = Tk()
root.geometry(str(w)+"x"+str(h)) # geometry() expects a string "WIDTHxHEIGHT"
c = Canvas(root, height=h, width=w, bg="black")
c.pack()
data = []

m = 0 # y = mx+b
b = 0

def remap(old_value, old_min, old_max, new_min, new_max):
    return (((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

class Point:
    # Object that holds information about all the points
    def __init__(self, x, y):
        self.mouse_x = x
        self.mouse_y = y
        self.norm_x = remap(self.mouse_x, 0, w, 0, 1)
        self.norm_y = remap(self.mouse_y, 0, h, 1, 0)

def draw_line(m,b):
    global id
    x1 = 0
    y1 = m * x1 +b
    x2 = 1
    y2 = m * x2 + b
    x1 = remap(x1, 0, 1, 0, w)
    x2 = remap(x2, 0, 1, 0, w)
    y1 = remap(y1, 0, 1, h, 0)
    y2 = remap(y2, 0, 1, h, 0)
    if m < 0:
        id = c.create_line(x1, y1, x2, y2, fill="red")
    else:
        id = c.create_line(x1, y1, x2, y2, fill="green")

def linear_reg():
    xsum = 0
    ysum = 0
    for point in data:
        xsum += point.norm_x
        ysum += point.norm_y
    xmean = xsum / len(data)
    ymean = ysum / len(data)
    num = 0
    den = 0
    for point in data:
        num += (point.norm_x - xmean) * (point.norm_y - ymean)
        den += (point.norm_x - xmean) * (point.norm_x - xmean)
    m = num / den
    b = ymean - m * xmean
    print(m, "x +", b)
    return m, b

def draw():
    for point in data:
        c.create_oval(point.mouse_x - 5, point.mouse_y - 5 , point.mouse_x + 5, point.mouse_y + 5, fill="white")
    if len(data) > 1:
        c.delete(id)
        k = linear_reg()
        draw_line(k[0], k[1])
    c.pack()
      
def left_click(event):
    point = Point(event.x, event.y)
    data.append(point)
    draw()

root.bind("<Button 1>", left_click)
root.mainloop()
