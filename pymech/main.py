
import time

import numpy as np

from pymech import graphics
from pymech.settings import global_settings


SCALE = global_settings['physics'].getint('pixels_per_metre')
GRAV = 9.81


class PositionScaledObject:
    """Handles conversions between screen and physical coordinates."""

    def __init__(self, screen_coords):
        self.pix_per_metre = SCALE
        self._screen_coords = np.array(screen_coords)
        self._position = None

    @property
    def position(self):
        return self._screen_coords / self.pix_per_metre

    @position.setter
    def position(self, position):
        self._position = position
        self._screen_coords = self._position * self.pix_per_metre

    @property
    def screen_coords(self):
        return self._screen_coords


class DisplayEntity:
    def __init__(self, physics, appearance):
        self.physics = physics
        self.drawn_objects = [appearance] + [graphics.Spring(s)
                                             for s in self.physics.springs]
        self.last_update = None

    def initial_draw(self, canvas):
        for d in self.drawn_objects:
            d.initial_draw(canvas, self.physics.screen_coords)
        self.last_update = time.time()

    def update(self, canvas):
        dt = time.time() - self.last_update
        position_delta = self.physics.calculate_motion(dt)
        self.last_update = time.time()

        for d in self.drawn_objects:
            d.move(canvas, position_delta * SCALE)
