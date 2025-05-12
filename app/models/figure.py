from .region import Region


class Figure:
    def hasL(self, region: Region) -> bool:
        l_shapes = [
            [(0, 0), (1, 0), (2, 0), (2, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 0)],
            [(0, 1), (1, 1), (2, 1), (2, 0)],
            [(1, 0), (1, 1), (1, 2), (0, 2)],
            [(0, 0), (1, 0), (1, 1), (1, 2)],
            [(0, 2), (1, 2), (1, 1), (1, 0)],
            [(0, 0), (0, 1), (1, 1), (2, 1)],
            [(0, 1), (0, 0), (1, 0), (2, 0)],
            [(0, 0), (0, 1), (1, 0), (2, 0)],
        ]
        return self._hasAny(region, "L", l_shapes)

    def hasT(self, region: Region) -> bool:
        t_shapes = [
            [(0, 1), (1, 0), (1, 1), (2, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 1)],
            [(0, 0), (1, 0), (1, 1), (2, 0)],
            [(0, 1), (1, 0), (1, 1), (1, 2)],
        ]
        return self._hasAny(region, "T", t_shapes)

    def hasI(self, region: Region) -> bool:
        i_shapes = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 0), (0, 1), (0, 2), (0, 3)],
        ]
        return self._hasAny(region, "I", i_shapes)

    def hasS(self, region: Region) -> bool:
        s_shapes = [
            [(0, 1), (0, 2), (1, 0), (1, 1)],
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(0, 0), (0, 1), (1, 1), (1, 2)],
            [(0, 1), (1, 0), (1, 1), (2, 0)],
        ]
        return self._hasAny(region, "S", s_shapes)

    def _hasAny(
        self, region: Region, value: str, shapes: list[list[tuple[int, int]]]
    ) -> bool:
        min_row = min(cell.row for cell in region.cells)
        min_col = min(cell.col for cell in region.cells)
        normalized = sorted(
            [(cell.row - min_row, cell.col - min_col) for cell in region.cells]
        )
        board = region.cells[0].board
        if normalized in shapes:
            # Verificar se algum vizinho direto já tem essa figura
            for cell in region.cells:
                adjacents_values = board.adjacent_values(cell.row, cell.col)
                if value in adjacents_values:
                    return False  # Encontrou um vizinho com a figura que não pode ser colocada

            # Verificar se ao colocar a figura, um bloco 2x2 seria formado
            return self.can_place_figure_without_2x2(region, value)

        return False

    def can_place_figure_without_2x2(self, region, value):
        simulated = set((cell.row, cell.col) for cell in region.cells)

        if not region.cells or not region.cells[0].board:
            return False
        board = region.cells[0].board

        def is_2x2_block_filled(r, c):
            coords = [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]
            for row, col in coords:
                # Se a célula está na simulação, consideramos que ficará com alguma figura
                if (row, col) in simulated:
                    continue
                cell = board.get_cell(row, col)
                if not cell or cell.figure is None:
                    return (
                        False  # Ainda há célula vazia, então não é um bloco 2x2 cheio
                    )
            return True  # Todas estão ocupadas

        for cell in region.cells:
            for dr in [-1, 0]:
                for dc in [-1, 0]:
                    r, c = cell.row + dr, cell.col + dc
                    if is_2x2_block_filled(r, c):
                        return False  # Encontrou bloco 2x2 cheio

        # Se não formar nenhum 2x2 totalmente cheio, aplica a figura
        for cell in region.cells:
            cell.set_figure(value)
        return True
