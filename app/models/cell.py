class Cell:
    def __init__(
        self,
        row,
        col,
        region_id,
    ):
        self.col = col
        self.row = row
        self.region_id = region_id
        self.figure = None  # figura atribuída

    def __repr__(self):
        return f"{self.figure if self.figure else self.region_id} "

    def set_figure(self, value):
        self.figure = value
