from .region import Region
from .cell import Cell
from sys import stdin


class Board:
    """Representação interna de um tabuleiro do Puzzle Nuruomino."""

    def __init__(self, text: str):
        self.board = []
        self.regions = {}
        self._parseInstance(text)

    def adjacent_regions(self, region: Region) -> list:
        """Devolve uma lista das regiões que fazem fronteira com a região passada como argumento."""
        adjacent_regions = set()  # Usando um set para evitar duplicação

        # Obter todas as células da região
        region_cells = {(cell.row, cell.col) for cell in region.cells}

        for other_region in self.regions.values():
            if other_region.id != region.id:
                # Verificar se alguma célula de region está adjacente a alguma célula de other_region
                for cell in other_region.cells:
                    for dr, dc in [
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1),
                    ]:  # Direções: cima, baixo, esquerda, direita
                        adjacent_row, adjacent_col = cell.row + dr, cell.col + dc
                        if (adjacent_row, adjacent_col) in region_cells:
                            adjacent_regions.add(
                                other_region
                            )  # Usar .add() para evitar duplicação
                            break
                    else:
                        continue
                    break

        return list(adjacent_regions)  # Converter de volta para lista, se necessário

    def adjacent_positions(self, row: int, col: int) -> list:
        """Devolve as posições adjacentes à região, em todas as direções, incluindo diagonais."""
        return [
            (row + dr, col + dc)
            for dr in [-1, 0, 1]
            for dc in [-1, 0, 1]
            if (dr != 0 or dc != 0)
            and (0 <= row + dr < self.rows)
            and (0 <= col + dc < self.cols)
        ]

    def adjacent_values(self, row: int, col: int) -> list:
        """Devolve os valores das celulas adjacentes à região, em todas as direções, incluindo diagonais."""
        return [
            self.get_cell(row + dr, col + dc).value
            for dr in [-1, 0, 1]
            for dc in [-1, 0, 1]
            if (dr != 0 or dc != 0)
            and (0 <= row + dr < self.rows)
            and (0 <= col + dc < self.cols)
        ]

    @staticmethod
    def parse_instance():
        """Lê o texto do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt

            > from sys import stdin
            > line = stdin.readline().split()
        """
        text = stdin.read()
        return Board(text)

    def _parseInstance(self, instance: str) -> None:
        lines = instance.strip().split("\n")
        self.rows = len(lines)
        self.cols = len(lines[0].split())
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.regions = {}  # Agora será um dicionário

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

            self.regions[region_id] = Region(region_id, cells)

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.board[row][col]
        return None

    def __repr__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.board)
