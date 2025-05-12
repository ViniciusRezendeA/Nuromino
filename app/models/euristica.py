from .board import Board
from .figure import Figure
from .region import Region


class Euristica:
    def __init__(self, board: Board):
        self.board = board

    def resolveBoard(self) -> None:
        """Resolve as regiões com 4 células, se possível."""
        for (
            region
        ) in self.board.regions.values():  # Acessa diretamente os objetos Region
            if region.size == 4:
                self.__checkIsSomeFigure(
                    region
                )  # Aqui você pode passar o objeto Region
            if region.size == 5:
                pass  # Lógica para quando a região tem 5 células
            else:
                pass  # Lógica para outras situações

    def __checkIsSomeFigure(self, region: Region) -> bool:
        """Verifica se a região já tem uma figura atribuída."""
        Figure().hasL(region) or Figure().hasT(region) or Figure().hasI(
            region
        ) or Figure().hasS(region)
