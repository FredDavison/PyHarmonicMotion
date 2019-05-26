
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
        self.constraints = []
        self.dampers = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def add_damper(self, damper):
        self.dampers.append(damper)

    def resolve_external_forces(self):
        f_grav = self.mass * GRAV
        f_spring = sum([c.resistance(self.position) for c in self.constraints])
        f_damping = sum([d.resistance(self.velocity) for d in self.dampers])
        return sum([f_grav, f_spring, f_damping])

    def calculate_motion(self, dt):
        external_force = self.resolve_external_forces()
        a = external_force / self.mass
        self.velocity = self.velocity + a * dt
        pos_delta = (self.velocity * dt) * self.pix_per_metre
        self.position = self.position + pos_delta
        return pos_delta
