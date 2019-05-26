
import tkinter as tk
import time
import math


PI = math.pi


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-topmost', True)

    W = 800
    H = 800
    pixels_per_metre = 100

    canvas = tk.Canvas(root, width=W, height = H)
    canvas.pack()

    neutral_x = W / 2
    neutral_y = H / 2
    radius = 10

    A = 100 # amplitude pixels
    k = 250 # spring stiffness
    m = 10 # mass
    c = 6 # damping

    ang_freq = (k / m) ** (-1 / 2)
    T = 2 * PI * (k / m) ** ang_freq

    dt = .05

    start_x = neutral_x + A
    start_v = 0
    x = start_x
    v = start_v

    shape1 = canvas.create_oval(start_x-radius, neutral_y-radius,
                                start_x+radius, neutral_y+radius,
                                outline='white', fill='blue', tag='shape1')
    centre_line = canvas.create_line(neutral_x, neutral_y+10,
                                     neutral_x, neutral_y-10,
                                     fill='grey')
    fix_line = canvas.create_line(neutral_x, neutral_y,
                                  x, neutral_y, fill='grey')

    canvas.update()

    start_t = time.time()
    while True:
        fk = (x - neutral_x) * k
        fi = -fk
        fd = -c * v
        f = fi + fd
        a = f / m
        v = v + a * dt
        prev_x = x
        dx = v * dt
        x = x + dx


        print('{:6.0f}{:6.2f}{:6.2f}'.format(x-neutral_x, v, a), end='\r')
        canvas.after(20)
        canvas.coords(fix_line, neutral_x, neutral_y, x, neutral_y)
        canvas.move('shape1', dx, 0)
        canvas.tag_raise(shape1)
        canvas.update()

    root.mainloop()
