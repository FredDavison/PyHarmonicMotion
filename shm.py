from __future__ import division

import Tkinter as tk
import time
import math

PI = math.pi


def animation(v):
    while True:
        print v
        y = 0
        for i in range(0,51):
            time.sleep(0.025)
            canvas.move(shape1, v, y)
            canvas.update()


if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height = 400)
    canvas.pack()

    start_x = 200
    start_y = 200
    shape1 = canvas.create_oval(start_x-20, start_y-20, start_x+20, start_y+20, outline='white', fill='blue', tag='shape1')

    A = 100 # amplitude pixels
    k = 1
    m = 10
    ang_freq = (k / m) ** (-1 / 2)
    T = 2 * PI * (k / m) ** ang_freq
    dx = 0
    prev_x = start_x

    start_t = time.time()
    while True:
        t = time.time() - start_t
        x = A * math.cos(ang_freq * t) + start_x
        dx = x - prev_x
        print t, ang_freq * t, x, dx
        canvas.after(20)
        canvas.move('shape1', dx, 0)
        canvas.update()
        prev_x = x

    root.mainloop()
