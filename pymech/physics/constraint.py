import numpy as np

class LinearSpring:
    """Provides spring force equal to displacement times stiffness."""

    def __init__(self, position, stiffness):
        self.position = position
        self.k = np.asarray(stiffness)

    def resistance(self, target_position):
        displacement = self.position - target_position
        return displacement * self.k


class ViscousDamper:
    """Provides damping force equal to velocity times damping constant."""

    def __init__(self, damping_constant):
        self.c = np.asarray(damping_constant)

    def resistance(self, velocity):
        return velocity * self.c * -1
