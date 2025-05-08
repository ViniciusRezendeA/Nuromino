from models.Board import Board
from models.Figure import Figure
from models.Region import Region


class Euristica:
    def __init__(self, board: Board):
        self.board = board

    def resolveBoard(self) -> None:
        """Resolve as regiões com 4 células, se possível."""
        for region in self.board.regions:
            if region.size == 4:
                self.__checkIsSomeFigure(region)
            if region.size == 5:
                pass
            else:
                pass

    def __checkIsSomeFigure(self, region: Region) -> bool:
        """Verifica se a região já tem uma figura atribuída."""
        Figure().hasL(region) or Figure().hasT(region) or Figure().hasI(
            region
        ) or Figure().hasS(region)
