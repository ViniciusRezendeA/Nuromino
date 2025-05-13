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
            if region.size == 4:
                self._fillRegionWitSize4(
                    region
                )  # Aqui você pode passar o objeto Region
            else:
                Figure().fill_region(region)

    def _fillRegionWitSize4(self, region: Region) -> bool:
        """Verifica se a região já tem uma figura atribuída."""
        Figure().hasL(region) or Figure().hasT(region) or Figure().hasI(
            region
        ) or Figure().hasS(region)

    def _checkAllRegionIsConnected(self, board: Board) -> bool:
        """Verifica se todas as regiões estão conectadas."""
