__author__ = 'Taciane'

from Cell import Cell
class Ocean(Cell):

    def __str__(self):
        if (self.is_destroyed):
            return "A"
        return  "O"

    def is_battleship(self):
        return False