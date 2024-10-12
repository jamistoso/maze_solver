import random
from time import sleep


from cell import Cell
from window import Window



class Maze():

    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            self.seed = seed
            random.seed(self.seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell() for j in range(self.num_rows)] for i in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x_val_1 = self.x1 + (i * self.cell_size_x)
        y_val_1 = self.y1 + (j * self.cell_size_y)
        x_val_2 = x_val_1 + self.cell_size_x
        y_val_2 = y_val_1 + self.cell_size_y
        self._cells[i][j].draw(x_val_1, x_val_2, y_val_1, y_val_2, self.win)
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
            for val in directions:
                x_ind = val[0] + i
                if x_ind < 0 or x_ind >= self.num_cols:
                    continue
                y_ind = val[1] + j
                if y_ind < 0 or y_ind >= self.num_rows:
                    continue
                if not self._cells[x_ind][y_ind].visited:
                    to_visit.append((x_ind, y_ind))
            if to_visit == []:
                return
            else:
                direction = random.randrange(0, len(to_visit))
                chosen_cell = to_visit[direction]
                if chosen_cell == (i-1, j):
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(i-1, j)
                elif chosen_cell == (i+1, j):
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(i+1, j)
                elif chosen_cell == (i, j-1):
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(i, j-1)
                elif chosen_cell == (i, j+1):
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(i, j+1)
                self._break_walls_r(chosen_cell[0], chosen_cell[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
        
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # down
        if j != self.num_rows - 1 and not self._cells[i][j+1].visited and not current.has_bottom_wall:
            current.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j + 1):
                return True
            current.draw_move(self._cells[i][j+1], undo=True)

        # right
        if i != self.num_cols - 1 and not self._cells[i+1][j].visited and not current.has_right_wall:
            current.draw_move(self._cells[i+1][j])
            if self._solve_r(i + 1, j):
                return True
            current.draw_move(self._cells[i+1][j], undo=True)

        # up
        if j != 0 and not self._cells[i][j-1].visited and not current.has_top_wall:
            current.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j - 1):
                return True
            current.draw_move(self._cells[i][j-1], undo=True)

        # left
        if i != 0 and not self._cells[i-1][j].visited and not current.has_left_wall:
            current.draw_move(self._cells[i-1][j])
            if self._solve_r(i - 1, j):
                return True
            current.draw_move(self._cells[i-1][j], undo=True)

        return False