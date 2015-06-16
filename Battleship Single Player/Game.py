__author__ = 'Taciane'

from Board import Board
import random

class Game():
    def __init__(self):
            self.set_up()
            self.endMessage = ""
            self.start()

    def set_up(self):
        while True:
            try:
                rows = int(raw_input ("Number of rows: "))
                cols = int(raw_input ("Number of cols: "))
                rounds = int(raw_input ("Number of rounds: "))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
        self.board = Board (rows, cols)
        self.rounds = rounds
        reference = rows*cols
        if (reference > 16):
            number_ships = random.randint(reference/3,reference/2)
        else:
            number_ships = random.randint(1, min(rows, cols))
        self.board.set_ships (number_ships)

    """def is_victory(self):
           destroyed = 0
           for r in range(self.board.rows):
               for c in range(self.board.cols):
                   if (self.board.positions[(r,c)].is_battleship() and self.board.positions[(r,c)].is_destroyed):
                       destroyed +=1
           if (destroyed == self.board.number_ships_cells()):
               self.end_message = "Congratulations! ;D"
               return True
           else:
               self.endMessage = "Game Over! :("
           return False"""

    def is_victory(self):
          destroyed = 0
          for ship in self.board.ships:
                  if (ship.is_destroyed()):
                      destroyed +=1
          if (destroyed == self.board.number_ships()):
              self.end_message = "Congratulations! ;D"
              return True
          else:
              self.endMessage = "Game Over! :("
          return False

    def start(self):
          self.board.print_board()
          while (self.rounds > 0 and not self.is_victory()):
             guessRow=0
             guessCol=0
             while (guessRow > self.board.rows or guessCol > self.board.cols or \
                    guessRow <= 0 or guessCol <= 0):
                try:
                    guessRow = int(raw_input ("Row: "))
                    guessCol = int(raw_input ("Col: "))
                    break
                except ValueError:
                    print "Oops!  That was no valid number.  Try again..."
             try:
                 if (not self.board.positions[(guessRow-1, guessCol-1)].is_destroyed):
                    self.board.positions[(guessRow-1, guessCol-1)].resolve_shot()
                    self.board.print_board()
                    self.rounds -= 1
                 else:
                    print "Position already marked! KADOING!"
             except KeyError:
                print "Position out of board! >.>"
          self.is_victory()
          self.print_end_message()
          self.print_new_game()

    def print_end_message(self):
           print self.end_message

    def print_new_game(self):
        input = "BOO"
        while(not (input == "Y" or input == "y" or input == "" or input == "N" or input == "n")):
             input = raw_input("Would you like to play again? ^_^ [Y/n]")
        if (input == "Y" or input == "y" or input == ""):
            self.set_up()
            self.start()
        else:
            print "Smell ya later!"




















