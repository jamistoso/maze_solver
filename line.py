class Line():
    p1 = None
    p2 = None


    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def draw(self, canvas, fill_color):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )