import unittest

from index import TicTacToe

class TicTacToeTest(unittest.TestCase):
    """Unit test for Tic-Tac-Toe."""
    def test_inputs_should_between_zero_and_two(self):
        tic_tac_toe = TicTacToe()

        self.assertEqual(tic_tac_toe.is_valid_input(-1, -1), False)
        self.assertEqual(tic_tac_toe.is_valid_input(0, 0), True)
        self.assertEqual(tic_tac_toe.is_valid_input(3, 3), False)

    def test_game_should_detect_non_empty_horizontal_winning_pattern(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board.matrix = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]

        self.assertEqual(tic_tac_toe.has_horizontal_win_pattern(), True)

        tic_tac_toe.board.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.assertEqual(tic_tac_toe.has_horizontal_win_pattern(), False)

    def test_game_should_detect_non_empty_vertical_winning_pattern(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board.matrix = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]

        self.assertEqual(tic_tac_toe.has_vertical_win_pattern(), True)
        
        tic_tac_toe.board.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.assertEqual(tic_tac_toe.has_vertical_win_pattern(), False)