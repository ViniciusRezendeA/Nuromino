from .board import Board
from .figure import Figure
from .region import Region


class Euristica:
    def __init__(self, board: Board):
        self.board = board

    def resolveBoard(self) -> None:
        self.board.regions = self.board.regions
        """Resolve as regiões com 4 células, se possível."""
        for (
            region
        ) in self.board.regions.values():  # Acessa diretamente os objetos Region

            Figure().fill_region(region)
