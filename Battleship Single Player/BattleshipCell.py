__author__ = 'Taciane'

from Cell import Cell
class BattleshipCell(Cell):

    def __str__(self):
        if (self.is_destroyed):
            return "B"
        return  "O"

    def is_battleship(self):
        return True