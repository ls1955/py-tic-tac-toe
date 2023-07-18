import unittest

from index import TicTacToe

class GameBoardTest(unittest.TestCase):
    """Unit test for GameBoard."""
    def test_game_board_is_full_if_no_empty_slot(self):
        board = TicTacToe.GameBoard()
        board.matrix = [["X", "X", "X"], ["O", "O", "O"], ["X", "X", "X"]]

        self.assertEqual(board.is_full(), True)
        