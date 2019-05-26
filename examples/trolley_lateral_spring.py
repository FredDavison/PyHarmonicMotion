
from pymech import DisplayEntity
from pymech.physics import PhysicsObject, LinearSpring, ViscousDamper
from pymech.graphics import Circle, animate_entities


def main():
    circle = Circle(radius=10)
    trolley = PhysicsObject(position=[400, 0, 400], mass=100)
    trolley.degrees_of_freedom = [1, 1, 0]

    spring = LinearSpring(position=[500, 0, 400], stiffness=[25, 0, 0])
    damper = ViscousDamper(damping_constant=[0, 0, 0])
    trolley.add_spring(spring)
    trolley.add_damper(damper)
    display = DisplayEntity(physics=trolley, appearance=circle)
    animate_entities([display])


if __name__ == '__main__':
    main()
