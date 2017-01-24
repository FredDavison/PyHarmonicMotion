from Tkinter import *
import time
import math


def animation(v):
    while True:
        print v
        y = 0
        for i in range(0,51):
            time.sleep(0.025)
            canvas.move(shape1, v, y)
            canvas.update()


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=400, height = 400)
    canvas.pack()
    shape1 = canvas.create_oval(180, 180, 220, 220, outline='white', fill='blue', tag='shape1')

    max_v = 6 # pixels per second
    dx = 0
    dy = 0
    start_t = time.time()
    while True:
        canvas.move('shape1', dx, dy)
        canvas.after(20)
        canvas.update()
        elapsed_t = time.time() - start_t
        dx = math.cos((elapsed_t % 5) / 5 * 2 * math.pi) * max_v
        print dx

    root.mainloop()
