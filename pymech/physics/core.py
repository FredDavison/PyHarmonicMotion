
import numpy as np

from pymech.settings import global_settings


GRAV = np.array([0., 0., 9.81])
SCALE = global_settings['physics'].getint('pixels_per_metre')


class PhysicsObject:
    def __init__(self, position, mass):
        self._dof = None
        self.degrees_of_freedom = np.array([True, True, True], dtype=bool)
        self.pix_per_metre = SCALE
        self.position = np.array(position)
        self.velocity = np.array([0, 0, 0])
        self.acceleration = np.array([0, 0, 0]) # not used
        self.mass = mass
        self.springs = []
        self.dampers = []

    @property
    def degrees_of_freedom(self):
        return self._dof

    @degrees_of_freedom.setter
    def degrees_of_freedom(self, dofs):
        # validation maybe
        self._dof = np.asarray(dofs, dtype=bool)

    def add_spring(self, constraint):
        self.springs.append(constraint)

    def add_damper(self, damper):
        self.dampers.append(damper)

    def resolve_external_forces(self):
        f_grav = self.mass * GRAV
        f_spring = sum([c.resistance(self.position) for c in self.springs])
        f_damping = sum([d.resistance(self.velocity) for d in self.dampers])
        return sum([f_grav, f_spring, f_damping])

    def calculate_motion(self, dt):
        external_force = self.resolve_external_forces()
        a = external_force / self.mass * self._dof
        self.velocity = self.velocity + a * dt
        pos_delta = (self.velocity * dt) * self.pix_per_metre
        self.position = self.position + pos_delta
        self.acceleration = a
        return pos_delta
