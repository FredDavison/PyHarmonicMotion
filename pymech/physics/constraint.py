
import numpy as np

from pymech.main import PositionScaledObject
from pymech.settings import global_settings


SCALE = global_settings['physics'].getint('pixels_per_metre')


class LinearSpring(PositionScaledObject):
    """Provides spring force equal to displacement times stiffness."""

    def __init__(self, position, stiffness):
        super().__init__(position)
        self.k = np.asarray(stiffness)

    def resistance(self, target_position):
        displacement = self.position - target_position
        return displacement * self.k


class AxialSpring(PositionScaledObject):
    """Provides linear spring force in direction of its axial extension."""

    def __init__(self, position, stiffness):
        super().__init__(position)
        self.k = np.asarray(stiffness)

    def resistance(self, target_position):
        displacement = self.position - target_position
        extension = np.linalg.norm(displacement)
        resistance = extension * self.k
        return resistance * displacement


class ViscousDamper:
    """Provides damping force equal to velocity times damping constant."""

    def __init__(self, damping_constant):
        self.c = np.asarray(damping_constant)

    def resistance(self, velocity):
        return velocity * self.c * -1
