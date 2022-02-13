import pytest
import numpy as np
from sudoku import evaluate


def test_nonsquare_grid():
    grid = np.random.randint(1, 4, (2, 3))
    with pytest.raises(ValueError):
        evaluate.is_grid_valid(grid)


def test_nonsquare_n():
    grid = np.random.randint(1, 5, (5, 5))
    with pytest.raises(ValueError):
        evaluate.is_grid_valid(grid)


def test_valid_grid():
    grid = np.array([[1, 2, 3, 4],
                     [3, 4, 1, 2],
                     [2, 1, 3, 4],
                     [4, 3, 2, 1]])
    assert evaluate.is_grid_valid(grid) is True


def test_invalid_box():
    grid = np.array([[1, 2, 3, 4],
                     [4, 3, 1, 2],
                     [2, 1, 3, 4],
                     [4, 3, 2, 1]])
    assert evaluate.is_grid_valid(grid) is False


def test_invalid_row():
    grid = np.array([[1, 2, 1, 3],
                     [3, 4, 1, 2],
                     [2, 1, 3, 4],
                     [4, 3, 2, 1]])
    assert evaluate.is_grid_valid(grid) is False


def test_invalid_column():
    grid = np.array([[1, 2, 3, 4],
                     [3, 4, 1, 2],
                     [1, 1, 3, 4],
                     [4, 3, 2, 1]])
    assert evaluate.is_grid_valid(grid) is False


def test_get_box():
    grid = np.array([[1, 2, 3, 4],
                     [3, 4, 1, 2],
                     [2, 1, 3, 4],
                     [4, 3, 2, 1]])

    b1 = np.array([[1, 2], [3, 4]])
    b2 = np.array([[3, 4], [1, 2]])
    b3 = np.array([[2, 1], [4, 3]])
    b4 = np.array([[3, 4], [2, 1]])

    se = evaluate.SudokuEvaluator(4)

    np.testing.assert_array_equal(se.get_box(grid, 0, 0), b1)
    np.testing.assert_array_equal(se.get_box(grid, 0, 1), b2)
    np.testing.assert_array_equal(se.get_box(grid, 1, 0), b3)
    np.testing.assert_array_equal(se.get_box(grid, 1, 1), b4)
