import Board


class NuruominoState:
    state_id = 0

    def __init__(self, board: Board):
        self.board = board
        self.id = Nuroumino.state_id
        Nuroumino.state_id += 1

    def __lt__(self, other):

        return self.id < other.id
