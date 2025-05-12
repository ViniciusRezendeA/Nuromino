from .board import Board


class NuruominoState:
    state_id = 0

    def __init__(
        self,
        board: Board,
        nuromino,
    ):
        self.board = board
        self.id = nuromino.state_id
        nuromino.state_id += 1

    def __lt__(self, other):
        """Este método é utilizado em caso de empate na gestão da lista
        de abertos nas procuras informadas."""
        return self.id < other.id
