
import numpy as np

from pymech import Entity, PhysicsObject, DisplayObject, animate_entities


class FreeMass(PhysicsObject):
    def __init__(self, position):
        super().__init__(self)


def main():
    mass = PhysicsObject(position=[400, 0, 0],
                         mass=10)
    display = DisplayObject(mass, None)
    animate_entities([display])



if __name__ == '__main__':
    main()
