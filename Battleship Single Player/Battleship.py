__author__ = 'Taciane'

from BattleshipCell import BattleshipCell

class Battleship():

    def __init__(self, cells): #cells = list of positions
        self.destroyed = False
        self.cells = cells

    def is_destroyed(self):
        total = 0
        for ship in self.cells:
            if (ship.is_destroyed):
                total +=1

        if(total == len(self.cells)):
            self.destroyed = True
            return True
        return False

    def __str__(self, cell): #NAO CHAMADO!?!?
        if (cell in self.cells):
            cell.__str__()

    def resolve_shot(self,cell): #NAO CHAMADO!?!?
        cell.resolve_shot()
