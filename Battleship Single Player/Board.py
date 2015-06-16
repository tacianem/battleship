__author__ = 'Taciane'

from Ocean import Ocean
from BattleshipCell import BattleshipCell
from Battleship import Battleship

import random

class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.positions = dict()
        self.ships =[] #list of ships
        print "Welcome on board, fella!"
        for row in range(self.rows):
            for col in range(self.cols):
                cell = Ocean(row,col) #just water
                self.positions[(row, col)] = cell

    def print_board (self):
        for row in range (self.rows):
            for col in range(self.cols):
                print self.positions[(row, col)],
            print "\n",


    """def set_number_ships (self,number_ships): #SO UMA CELL CADA BARCO, FIRST THINGS FIRST!
        for n in range(number_ships):
            row = random.randint(0,self.rows-1)
            col = random.randint(0,self.cols-1)
            if(not self.positions[(row,col)].is_battleship()):
                self.positions[(row,col)] = BattleshipCell(row, col)
                self.ships +=1
            else:
                n-=1"""


    def number_ships(self):
            return len(self.ships)

    def set_ships(self, n):
        for i in range(n):
            direction = random.randint(1,2) #1 = vertical, 2 = horizontal

            initial_row = random.randint(0,self.rows-1)
            initial_col = random.randint(0,self.cols-1) #initial position

            if (direction == 1):
                tamanho = random.randint(1,self.rows-initial_row)
            else:
                tamanho = random.randint(1,self.cols-initial_col)

            aux = [] #cells
            count = 0
            row = initial_row
            col = initial_col
            for i in range(tamanho):
                if (not self.positions[(row,col)].is_battleship()):
                    count +=1
                if (direction == 1): #take next position
                    row+=1
                else:
                    col+=1
            if (count == tamanho):
                i = 0
                for i in range(tamanho):
                    if (direction == 1): #take next position
                        row=initial_row+i
                    else:
                        col=initial_col+i
                    self.positions[(row,col)] = BattleshipCell(row, col)
                    aux.append(self.positions[(row,col)])
                    i+=1
                self.ships.append(Battleship(aux))
            else:
                i-=1











