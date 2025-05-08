from models.Region import Region
from models.Cell import Cell


class Board:

    def __init__(self, text: str):
        self.board = []
        self.regions = []
        self.parseInstance(text)

    def adjacent_positions(self, row: int, col: int) -> list:
        pass

    def adjacent_values(self, row: int, col: int) -> list:
        """Devolve as posições adjacentes à região, em todas as direções,
        incluindo diagonais."""
        pass

    def adjacent_regions(self, region: int) -> list:
        """Devolve os valores das celulas adjacentes à região,
        em todas as direções, incluindo diagonais."""

    def parseInstance(self, instance: str) -> None:

        lines = instance.strip().split("\n")
        self.rows = len(lines)
        self.cols = len(lines[0].split())
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.regions = []

        discoveryRegions = {}
        for row in range(self.rows):
            cells = list(map(int, lines[row].split()))
            for col in range(self.cols):
                cell_value = cells[col]
                cell = Cell(row, col, cell_value, self)
                self.board[row][col] = cell
                if cell_value not in discoveryRegions:
                    discoveryRegions[cell_value] = []
                discoveryRegions[cell_value].append(cell)

        for region_id, cells in discoveryRegions.items():
            self.regions.append(Region(region_id, cells))

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.board[row][col]
        return None

    def __repr__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.board)
    