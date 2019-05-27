
from copy import deepcopy

from pymech import DisplayEntity
from pymech.physics import PhysicsObject, AxialSpring, ViscousDamper
from pymech.graphics import Circle, animate_entities


def main():
    circle = Circle(radius=10)
    particle = PhysicsObject(position=[380, 0, 400], mass=10)
    spring = AxialSpring(position=[400, 0, 400], stiffness=50)
    damper = ViscousDamper(damping_constant=[5, 5, 5])
    particle.add_spring(spring)
    particle.add_damper(damper)

    display = DisplayEntity(physics=particle, appearance=circle)
    animate_entities([display])


if __name__ == '__main__':
    main()
