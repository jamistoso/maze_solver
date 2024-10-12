from tkinter import Tk, BOTH, Canvas
from line import Line
from cell import Cell

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = 'Maze Solver'
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
    
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    
    def close(self):
        self.running = False


    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


    def draw_cell(self, cell):
        cell.draw()