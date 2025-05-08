class Cell:
    def __init__(self, row, col, region, board=None):
        self.col = col
        self.row = row
        self.region = region 
        self.board = board  # referência ao board
        self.figure = None  # figura atribuída

    def __repr__(self):
        return f"{self.figure if self.figure else self.region} "

    def set_figure(self, value):
        self.figure = value
