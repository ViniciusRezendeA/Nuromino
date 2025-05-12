class Cell:
    def __init__(
        self,
        row,
        col,
        region,
    ):
        self.col = col
        self.row = row
        self.region = region
        self.figure = None  # figura atribuída

    def __repr__(self):
        return f"{self.figure if self.figure else self.region} "

    def set_figure(self, value):
        self.figure = value
