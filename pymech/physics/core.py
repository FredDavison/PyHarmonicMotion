
import numpy as np

from pymech.settings import global_settings


GRAV = np.array([0., 0., 9.81])
SCALE = global_settings['physics'].getint('pixels_per_metre')


class PhysicsObject:
    def __init__(self, position, mass):
        self.pix_per_metre = SCALE
        self.position = np.array(position)
        self.velocity = np.array([0, 0, 0])
        self.acceleration = np.array([0, 0, 0])
        self.mass = mass

    def calculate_motion(self, dt):
        self.velocity = self.velocity + (GRAV * dt)
        pos_delta = (self.velocity * dt) * self.pix_per_metre
        self.position = self.position + pos_delta
        return pos_delta
