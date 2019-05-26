
from pymech import DisplayEntity
from pymech.physics import PhysicsObject, LinearSpring, ViscousDamper
from pymech.graphics import Circle, animate_entities


def main():
    circle = Circle(radius=10)
    mass = PhysicsObject(position=[400, 0, 300], mass=10)
    spring = LinearSpring(position=[400, 0, 400], stiffness=10)
    damper = ViscousDamper(damping_constant=10)
    mass.add_constraint(spring)
    mass.add_damper(damper)
    display = DisplayEntity(physics=mass, appearance=circle)
    animate_entities([display])


if __name__ == '__main__':
    main()
