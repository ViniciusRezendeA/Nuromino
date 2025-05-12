from .cell import Cell


class Region:
    def __init__(self, id: int, cells: list[Cell], board):
        self.id = id
        self.cells = cells
        self.size = len(cells)
        self.board = board

    def __repr__(self):
        return f"Region(id={self.id}, cells={self.cells})"
