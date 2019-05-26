
from pymech import DisplayEntity
from pymech.physics import PhysicsObject
from pymech.graphics import Circle, animate_entities


def main():
    mass = PhysicsObject(position=[400, 0, 0], mass=10)
    circle = Circle(radius=10)
    display = DisplayEntity(physics=mass, appearance=circle)
    animate_entities([display])


if __name__ == '__main__':
    main()
