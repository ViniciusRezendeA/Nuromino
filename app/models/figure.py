from .region import Region
from itertools import combinations


class Figure:
    def fill_region_with_figure(self, region: Region, value: str) -> bool:
        """
        Verifica se a figura pode ser colocada na região e, se possível, coloca a figura.
        """
        figureFormats = {
            "L": [
                [(0, 0), (1, 0), (2, 0), (2, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 0)],
                [(0, 1), (1, 1), (2, 1), (2, 0)],
                [(1, 0), (1, 1), (1, 2), (0, 2)],
                [(0, 0), (1, 0), (1, 1), (1, 2)],
                [(0, 2), (1, 2), (1, 1), (1, 0)],
                [(0, 0), (0, 1), (1, 1), (2, 1)],
                [(0, 1), (0, 0), (1, 0), (2, 0)],
                [(0, 0), (0, 1), (1, 0), (2, 0)],
            ],
            "T": [
                [(0, 1), (1, 0), (1, 1), (2, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 1)],
                [(0, 0), (1, 0), (1, 1), (2, 0)],
                [(0, 1), (1, 0), (1, 1), (1, 2)],
            ],
            "I": [
                [(0, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (0, 1), (0, 2), (0, 3)],
            ],
            "S": [
                [(0, 1), (0, 2), (1, 0), (1, 1)],
                [(0, 0), (1, 0), (1, 1), (2, 1)],
                [(0, 0), (0, 1), (1, 1), (1, 2)],
                [(0, 1), (1, 0), (1, 1), (2, 0)],
            ],
        }

        if value is None:
            for figure in figureFormats:
                if self._hasAny(region, figure, figureFormats[figure]):
                    return True
            return False
        else:
            return self._hasAny(region, value, figureFormats[value])

    def _hasAny(
        self, region: Region, value: str, shapes: list[list[tuple[int, int]]]
    ) -> bool:
        min_row = min(cell.row for cell in region.cells)
        min_col = min(cell.col for cell in region.cells)
        normalized = sorted(
            [(cell.row - min_row, cell.col - min_col) for cell in region.cells]
        )
        board = region.board
        if normalized in shapes:
            # Verifica se algum vizinho direto já tem essa figura
            for cell in region.cells:
                if value in board.adjacent_values(cell.row, cell.col):
                    return False
            # Verifica se ao colocar a figura, um bloco 2x2 seria formado
            return self.can_place_figure_without_2x2(region, value)

        return False

    def can_place_figure_without_2x2(self, region: Region, value: str) -> bool:
        simulated = set((cell.row, cell.col) for cell in region.cells)

        if not region.cells:
            return False
        board = region.board

        def is_2x2_block_filled(r, c):
            coords = [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]
            for row, col in coords:
                if (row, col) in simulated:
                    continue
                cell = board.get_cell(row, col)
                if not cell or cell.figure is None:
                    return False
            return True

        for cell in region.cells:
            for dr in [-1, 0]:
                for dc in [-1, 0]:
                    if is_2x2_block_filled(cell.row + dr, cell.col + dc):
                        return False

        for cell in region.cells:
            cell.set_figure(value)
        return True

    def fill_region(self, region: Region):
        used_cells = set()
        placed_any = True

        while placed_any:
            placed_any = False
            available_cells = [
                cell for cell in region.cells if (cell.row, cell.col) not in used_cells
            ]
            if len(available_cells) < 4:
                break

            for group in combinations(available_cells, 4):
                subregion = Region(region.id, list(group), region.board)
                if self.fill_region_with_figure(subregion, None):
                    for cell in group:
                        used_cells.add((cell.row, cell.col))
                    placed_any = True
                    break
