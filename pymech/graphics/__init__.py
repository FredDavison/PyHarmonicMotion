
import time
import tkinter as tk

from pymech.settings import global_settings


SETTINGS = global_settings['tkinter']


def animate_entities(entities):
    """Initialise and provide tkinter root."""

    height = SETTINGS.getint('height')
    width = SETTINGS.getint('width')

    root = tk.Tk()
    root.attributes('-topmost', 1)
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    canvas.update()
    root.attributes('-topmost', 0)

    draw_entities(canvas, entities)

    last_time = time.time()

    while True:
        dt = time.time() - last_time
        text_time = canvas.create_text(width / 2, 10, text=f'{dt:.2e}')

        update_entities(canvas, entities)
        canvas.after(1000 // 60)
        canvas.delete(text_time)
        last_time = time.time()


def draw_entities(canvas, entities):
    for entity in entities:
        entity.initial_draw(canvas)
    canvas.update()


def update_entities(canvas, entities):
    for entity in entities:
        entity.update(canvas)
    canvas.update()
