import window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = window.Window(1200,900)
    num_cols = 25
    num_rows = 25
    m1 = Maze(10, 10, num_rows, num_cols, 10, 10, win)
    m1.solve()
    win.wait_for_close()

main()