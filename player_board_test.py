import unittest

from index import TicTacToe

class PlayerBoardTest(unittest.TestCase):
    """Integration test between board and player."""
    def test_player_mark_a_symbol_on_board(self):
        player = TicTacToe.Player("tuna", "X")
        board = TicTacToe.GameBoard()

        player.mark(board, 0, 0)

        exp = [
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.assertEqual(board.matrix, exp)
