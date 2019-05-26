
import tkinter as tk

from pymech import global_settings



# SETTINGS = global_settings.items('tkinter')



def start_tk():
    """Initialise and provide tkinter root."""

    width, height = SETTINGS['width'], SETTINGS['height']

    root = tk.Tk()
    root.attributes('-topmost', True)

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    return root
