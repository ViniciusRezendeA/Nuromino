from models.Cell import Cell


class Region:
    def __init__(self, id: int, cells: list[Cell]):
        self.id = id
        self.cells = cells
        self.size = len(cells)

    def __repr__(self):
        return f"Region(id={self.id}, cells={self.cells})"

    def addFigure(self, figure: str) -> None:
        self.figure = figure
