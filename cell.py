from line import Line
from point import Point

class Cell():
    has_left_wall = True
    has_right_wall = True
    has_top_wall = True
    has_bottom_wall = True
    visited = False
    _x1 = None
    _x2 = None
    _y1 = None
    _y2 = None
    _win = None
    

    def draw(self, x1, x2, y1, y2, win=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        if win:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            if self.has_left_wall:
                left_wall.draw(self._win.canvas, 'black')
            else:
                left_wall.draw(self._win.canvas, 'white')

            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_wall = Line(p1, p2)
            if self.has_right_wall:
                right_wall.draw(self._win.canvas, 'black')
            else:
                right_wall.draw(self._win.canvas, 'white')

            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_wall = Line(p1, p2)
            if self.has_top_wall:
                top_wall.draw(self._win.canvas, 'black')
            else:
                top_wall.draw(self._win.canvas, 'white')

            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_wall = Line(p1, p2)
            if self.has_bottom_wall:
                bottom_wall.draw(self._win.canvas, 'black')
            else:
                bottom_wall.draw(self._win.canvas, 'white')


    def draw_move(self, to_cell, undo=False):
        self_mid_x = int(abs(self._x2 - self._x1) / 2)
        self_mid_y = int(abs(self._y2 - self._y1) / 2)
        self_point = Point(self_mid_x + self._x1, self_mid_y + self._y1) 
        to_mid_x = int(abs(to_cell._x2 - to_cell._x1) / 2)
        to_mid_y = int(abs(to_cell._y2 - to_cell._y1) / 2)
        to_point = Point(to_mid_x + to_cell._x1, to_mid_y + to_cell._y1)
        to_line = Line(self_point, to_point)
        line_color = 'gray' if undo else 'red'
        to_line.draw(self._win.canvas, line_color)