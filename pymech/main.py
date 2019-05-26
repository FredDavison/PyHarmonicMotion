
import time
from pymech import graphics


GRAV = 9.81


class DisplayEntity:
    def __init__(self, physics, appearance):
        self.physics = physics
        self.drawn_objects = [appearance] + [graphics.Spring(s)
                                             for s in self.physics.springs]
        self.last_update = None

    def initial_draw(self, canvas):
        for d in self.drawn_objects:
            d.initial_draw(canvas, self.physics.position)
        self.last_update = time.time()

    def update(self, canvas):
        dt = time.time() - self.last_update
        position_delta = self.physics.calculate_motion(dt)
        self.last_update = time.time()

        for d in self.drawn_objects:
            d.move(canvas, position_delta)
