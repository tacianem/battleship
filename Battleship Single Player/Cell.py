__author__ = 'Taciane'

class Cell():

    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.position = (row,col)
        self.is_destroyed = False

    def resolve_shot(self):
        self.is_destroyed=True


