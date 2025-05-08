from models.Board import Board
from models.Euristica import Euristica
from models.Figure import Figure
from models.Region import Region


class Main:
    def main():

        # Read the instance from the file
        with open("text.txt", "r") as file:
            instance = file.read()

        board = Board(instance)

        print("Board:")
        print(board)

        euristica = Euristica(board)
        euristica.resolveBoard()

        print("Board:")
        print(board)

        print("\nRegions:")
        for region in board.regions:
            print(region)

        print("-------------\n")

        print("Adjacents:")
        for region in board.regions:
            print(f"Region {region.id} Adjacents: {board.adjacent_regions(region.id)}")

    if __name__ == "__main__":
        main()
