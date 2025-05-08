from app.models import Board
from app.models import Euristica
from app.models import Region
from app.models import Figure

import os


class Main:
    def main():

        # Read the instance from the file
        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )  # Obtém o diretório atual do script
        file_path = os.path.join(base_dir, "boardTests", "test-01.txt")
        with open(file_path, "r") as file:
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
