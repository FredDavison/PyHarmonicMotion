from pymech.graphics.shapes import DrawnObject


class Spring(DrawnObject):
    def __init__(self, spring):
        self.tie_line = None
        self.spring = spring
        self.e_pos = None

    def initial_draw(self, canvas, entity_position):
        s_pos = self.spring.screen_coords
        e_pos = entity_position
        canvas.create_line(s_pos[0]+5, s_pos[2], s_pos[0]-5, s_pos[2])
        canvas.create_line(s_pos[0], s_pos[2]+5, s_pos[0], s_pos[2]-5)
        self.tie_line = canvas.create_line(s_pos[0], s_pos[2], e_pos[0], e_pos[2])
        self.e_pos = entity_position

    def move(self, canvas, position_delta):
        s_pos = self.spring.screen_coords
        e_pos = self.e_pos + position_delta
        canvas.coords(self.tie_line, s_pos[0], s_pos[2], e_pos[0], e_pos[2])
        self.e_pos = e_pos
