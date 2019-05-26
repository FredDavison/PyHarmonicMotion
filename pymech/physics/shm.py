
import tkinter as tk
import time
import math


PI = math.pi


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-topmost', True)

    W = 800
    H = 800

    canvas = tk.Canvas(root, width=W, height = H)
    canvas.pack()

    neutral_x = W / 2
    neutral_y = H / 2
    radius = 10

    A = 100 # amplitude pixels
    k = 1 # spring stiffness
    m = 10 # mass

    ang_freq = (k / m) ** (-1 / 2)
    T = 2 * PI * (k / m) ** ang_freq
    dx = 0
    start_x = 0#neutral_x + A
    prev_x = start_x

    shape1 = canvas.create_oval(start_x-radius, neutral_y-radius,
                                start_x+radius, neutral_y+radius,
                                outline='white', fill='blue', tag='shape1')
    canvas.update()

    start_t = time.time()
    while True:
        t = time.time() - start_t
        x = A * math.cos(ang_freq * t) + neutral_x
        dx = x - prev_x
        print(prev_x, dx, x, end='\r')
        canvas.after(20)
        canvas.move('shape1', dx, 0)
        canvas.update()
        prev_x = x

    root.mainloop()
