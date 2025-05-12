from models import Board
from models import Euristica
from models import Region
from models import Figure

import os
import sys


class Main:
    def main():
        board = None

        if len(sys.argv) > 1:
            # Read the instance from the file
            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )  # Obtém o diretório atual do script
            file_path = os.path.join(base_dir, sys.argv[1])
            with open(file_path, "r") as file:
                instance = file.read()

            board = Board(instance)
        else:
            board = Board.parse_instance()

        print("Board:")
        print(board)

        euristica = Euristica(board)
        euristica.resolveBoard()

        print("Board:")
        print(board)

        print("\nRegions:")
        for (
            region
        ) in board.regions.values():  # Iterar sobre os objetos Region completos
            print(region)

        print("-------------\n")

        print("Adjacents:")
        for (
            region
        ) in board.regions.values():  # Iterar sobre os objetos Region completos
            adjacents = [
                f"Region {adjacent_region.id}"
                for adjacent_region in board.adjacent_regions(region)
            ]
            print(f"Region {region.id} Adjacents: {', '.join(adjacents)}")

    if __name__ == "__main__":
        main()
