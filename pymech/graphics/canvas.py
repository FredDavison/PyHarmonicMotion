
import tkinter as tk

from pymech.settings import global_settings


SETTINGS = global_settings['tkinter']
WAIT_TIME = 1 // SETTINGS.getint('fps') * 1000


def canvas_setup():
    height = SETTINGS.getint('height')
    width = SETTINGS.getint('width')

    root = tk.Tk()
    root.attributes('-topmost', 1)
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    canvas.update()
    root.attributes('-topmost', 0)
    return canvas


def animate_entities(entities):
    """Initialise and provide tkinter root."""

    canvas = canvas_setup()
    draw_entities(canvas, entities)

    while True:
        update_entities(canvas, entities)
        canvas.after(WAIT_TIME)


def draw_entities(canvas, entities):
    for entity in entities:
        entity.initial_draw(canvas)
    canvas.update()


def update_entities(canvas, entities):
    for entity in entities:
        entity.update(canvas)
    canvas.update()
