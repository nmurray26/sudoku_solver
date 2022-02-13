import numpy as np


class SudokuEvaluator:
    def __init__(self, grid_size=9):
        if not np.sqrt(grid_size).is_integer():
            raise ValueError(f'Invalid grid size: {grid_size}.')

        self.grid_size = grid_size
        self.root = int(np.sqrt(grid_size))
        self.expected_numbers = np.linspace(1, grid_size, grid_size)

    def get_box(self, grid: np.array, i, j):
        istart, iend = self.root * i, self.root * i + self.root
        jstart, jend = self.root * j, self.root * j + self.root
        return grid[istart:iend, jstart:jend]

    def check_array(self, nums):
        for v in nums:
            if v not in self.expected_numbers:
                return False
        if len(set(nums)) != len(self.expected_numbers):
            return False
        return True

    def is_grid_valid(self, grid: np.array):
        if len(set(grid.shape)) != 1:
            raise ValueError(f'Invalid grid shape: {grid.shape}.')

        if grid.shape[0] != self.grid_size:
            raise ValueError('Invalid grid size.')

        for i in range(self.root):
            for j in range(self.root):
                # check the box
                box = self.get_box(grid, i, j)
                if not self.check_array(box.flatten()):
                    return False

            # check the row
            if not self.check_array(grid[i, :]):
                return False
            # check the column
            if not self.check_array(grid[:, i]):
                return False

        return True


def is_grid_valid(grid: np.array) -> bool:
    """
    Facade for SudokuEvaluator

    :param grid:
    :return:
    """
    su = SudokuEvaluator(grid.shape[0])
    return su.is_grid_valid(grid)
