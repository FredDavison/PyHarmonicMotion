
import time

import numpy as np


GRAV = 9.81


class DisplayEntity:
    def __init__(self, physics, appearance):
        self.physics = physics
        self.appearance = appearance
        self.last_update = None

    def initial_draw(self, canvas):
        self.appearance.initial_draw(self.physics.position, canvas)
        self.last_update = time.time()

    def update(self, canvas):
        dt = time.time() - self.last_update
        position_delta = self.physics.calculate_motion(dt)
        self.last_update = time.time()
        self.appearance.move(position_delta, canvas)
