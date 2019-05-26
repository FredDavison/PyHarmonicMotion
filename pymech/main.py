
import time

import numpy as np

from pymech.settings import global_settings
from pymech.graphics import animate_entities


GRAV = 9.81
VGRAV = np.array([0., 0., 9.81])
SCALE = global_settings['physics'].getint('pixels_per_metre')


class PhysicsObject:
    def __init__(self, position, mass):
        self.pix_per_metre = SCALE
        self.position = np.array(position)
        self.velocity = np.array([0, 0, 0])
        self.acceleration = np.array([0, 0, 0])
        self.mass = mass

    def calculate_motion(self, dt):
        self.velocity = self.velocity + (VGRAV * dt)
        pos_delta = (self.velocity * dt) * self.pix_per_metre
        self.position = self.position + pos_delta
        return pos_delta


class DisplayObject:
    def __init__(self, physics_object, draw_object):
        self.physics = physics_object
        self.drawer = draw_object

        self.last_update = None
        self.shape = None

    def update(self, canvas):
        dt = time.time() - self.last_update
        position_delta = self.physics.calculate_motion(dt)
        self.last_update = time.time()
        self._move(position_delta, canvas)
        canvas.update()

    def initial_draw(self, canvas):
        if self.shape:
            raise AttributeError("shape attribute already exists, initial_draw shouldn't be being called")
        pos = self.physics.position
        rad = 10
        self.shape = canvas.create_oval(pos[0]-rad, pos[2]-rad,
                                        pos[0]+rad, pos[2]+rad,
                                        outline='white', fill='blue')
        self.last_update = time.time()

    def _move(self, position, canvas):
        canvas.move(self.shape, position[0], position[2])
        canvas.tag_raise(self.shape)


class Entity:
    def __init__(self):
        self.scale = SCALE
        self.gravity = GRAV

        self.position = np.array([0, 0, 0])
        self.velocity = np.array([0, 0, 0])
        self.acceleration = np.array([0, 0, 0])
        self.mass = None

        self.shape = None
        self.last_update = None

    def initial_draw(self, canvas):
        raise NotImplementedError

    def move(self, canvas):
        raise NotImplementedError

    def calc_movement(self, dt):
        raise NotImplementedError


class TrolleyOnSpring(Entity):

    def __init__(self, neutral_y, neutral_x, start_x, spring_k, spring_c, mass):
        super(TrolleyOnSpring).__init__()
        self.neutral_x = neutral_x
        self.neutral_y = neutral_y
        self.start_x = start_x
        self.spring_k = spring_k
        self.spring_c = spring_c
        self.mass = mass
        self.x = start_x
        self.y = neutral_y
        self.dx = 0
        self.v = 0
        self.radius = 10
        self.start_line = None
        self.tie_line = None

    def initial_draw(self, canvas):
        self.shape = canvas.create_oval(self.x-self.radius, self.y-self.radius,
                                        self.x+self.radius, self.y+self.radius,
                                        outline='white', fill='blue')
        self.start_line = canvas.create_line(self.neutral_x, self.neutral_y+10,
                                             self.neutral_x, self.neutral_y-10,
                                             fill='grey')
        self.tie_line = canvas.create_line(self.neutral_x, self.neutral_y,
                                           self.start_x, self.neutral_y,
                                           fill='grey')
        self.last_update = time.time()

    def move(self, canvas):
        canvas.move(self.shape, self.dx, 0)
        canvas.coords(self.tie_line,
                      self.neutral_x, self.neutral_y,
                      self.x, self.neutral_y)
        canvas.tag_raise(self.shape)

    def calc_movement(self):
        dt = time.time() - self.last_update
        v, x = self.v, self.x

        fk = (x - self.neutral_x) * self.spring_k
        fi = -fk
        fd = -self.spring_c * v
        f = fd - fk #fi + fd
        a = f / self.mass
        v = v + a * dt
        dx = v * dt
        x = x + dx

        self.dx, self.x, self.v = dx, x, v
        self.last_update = time.time()


class WeightOnOneWaySpring(Entity):
    def __init__(self, neutral_y, neutral_x, start_y, spring_k, spring_c, mass):
        self.neutral_x = neutral_x
        self.neutral_y = neutral_y
        self.spring_k = spring_k
        self.spring_c = spring_c
        self.mass = mass
        self.radius = 10
        self.x = neutral_x
        self.y = start_y
        self.dy = 0
        self.v = 0
        self.start_line = None
        self.tie_line = None

    def initial_draw(self, canvas):
        self.shape = canvas.create_oval(self.x-self.radius, self.y-self.radius,
                                        self.x+self.radius, self.y+self.radius,
                                        outline='white',
                                        fill='blue')
        self.start_line = canvas.create_line(self.neutral_x+10, self.neutral_y,
                                             self.neutral_x-10, self.neutral_y,
                                             fill='grey')
        self.tie_line = canvas.create_line(self.neutral_x, self.neutral_y,
                                           self.neutral_x, self.y,
                                           fill='grey')
        canvas.tag_raise(self.shape)
        self.last_update = time.time()

    def move(self, canvas):
        canvas.move(self.shape, 0, self.dy)
        canvas.coords(self.tie_line,
                      self.neutral_x, self.neutral_y,
                      self.neutral_x, self.y)
        canvas.tag_raise(self.shape)
        self.last_update = time.time()

    def calc_movement(self):
        dt = time.time() - self.last_update
        v, y = self.v, self.y

        fk = -(y - self.neutral_y) / SCALE * self.spring_k
        fg = self.mass * GRAV
        fd = -self.spring_c * v
        f = fg + fk + fd
        a = f / self.mass
        v = v + a * dt
        dy = v * dt * SCALE
        y = y + dy
        print(f'fk: {fk:6.0f} fg: {fg:6.0f} fd: {fd:6.0f} f: {f:6.0f}', end='\r')

        self.dy, self.y, self.v = dy, y, v



def main():
    trolley = TrolleyOnSpring(neutral_y=400,
                              neutral_x=200,
                              start_x=100,
                              spring_k=450,
                              spring_c=10,
                              mass=10)
    mass = WeightOnOneWaySpring(neutral_y=400,
                                neutral_x=600,
                                start_y=300,
                                spring_k=150,
                                spring_c=15,
                                mass=20)
    entities = [trolley, mass]
    animate_entities(entities)


if __name__ == '__main__':
    main()
