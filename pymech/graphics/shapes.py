


class DrawnObject:

    def __init__(self):
        self.shape = None

    def initial_draw(self, canvas):
        raise NotImplementedError

    def _move(self, canvas):
        raise NotImplementedError


class Circle(DrawnObject):
    def __init__(self, radius, outline='white', fill='blue'):
        self.radius = radius
        self.outline = outline
        self.fill = fill

    def initial_draw(self, position, canvas):
        p, r = position, self.radius
        self.shape = canvas.create_oval(p[0]-r, p[2]-r,
                                        p[0]+r, p[2]+r,
                                        outline=self.outline,
                                        fill=self.fill)

    def move(self, position_delta, canvas):
        dp = position_delta
        canvas.move(self.shape, dp[0], dp[2])
        canvas.tag_raise(self.shape)
