
from pymech import DisplayEntity
from pymech.physics import PhysicsObject, LinearSpring, ViscousDamper
from pymech.graphics import Circle, animate_entities


def main():
    circle = Circle(radius=10)
    particle = PhysicsObject(position=[400, 0, 200], mass=20)
    spring = LinearSpring(position=[400, 0, 400], stiffness=[0, 0, 25])
    damper = ViscousDamper(damping_constant=[0, 0, 10])
    particle.add_spring(spring)
    particle.add_damper(damper)
    display = DisplayEntity(physics=particle, appearance=circle)
    animate_entities([display])


if __name__ == '__main__':
    main()
