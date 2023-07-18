class TicTacToe:
    """
    Tic-Tac-Toe game.
    Further reference: https://en.wikipedia.org/wiki/Tic-tac-toe
    """
    def __init__(self):
        self.player_one = TicTacToe.Player("player one", "X")
        self.player_two = TicTacToe.Player("player two", "O")
        self.is_player_one_turn = True
        self.board = TicTacToe.GameBoard()

    def run(self):
        """The main game loop that run until there is a winner."""
        counter = 2

        while counter:
            print(self.board)

            while True:
                x_coor = int(input(f"Please choose x coordinate, {self.curr_player().name}\n"))
                y_coor = int(input(f"Please choose y coordinate, {self.curr_player().name}\n"))

                if self.is_valid_input(x_coor, y_coor):
                    break
                print("The coordinates might be invalid or has already taken, please try again")
            self.curr_player.mark(self.board, x_coor, y_coor)

            # if (has_horizontal_win_pattern(x_coor, y_coor) or
            #     has_vertical_win_pattern(x_coor, y_coor) or
            #     has_diagonal_win_pattern(x_coor, y_coor)):
            #     # Return output and be done with it
            #     pass

            # Safety measure to prevent infinite loop
            counter -= 1

    def curr_player(self):
        """Return current player object for every turn."""
        return self.player_one if self.is_player_one_turn else self.player_two

    def is_valid_input(self, x, y):
        if not x in range(3) or not y in range(3):
            return False
        return self.board.matrix[x][y] == " "

    def has_horizontal_win_pattern(self):
        """See if any row in board have same player's symbol."""
        for row in self.board.matrix:
            if len(set(row)) == 1 and not row.count(" "):
                return True
        return False

    def has_vertical_win_pattern(self):
        """See if any column in board has same player's symbol."""
        matrix = self.board.matrix

        for col_index in range(len(matrix[0])):
            col = [matrix[row_index][col_index] for row_index in range(3)]

            if len(set(col)) == 1 and not col.count(" "):
                return True
        return False

    def has_diagonal_win_pattern(self):
        """See if two diagonl in board has same player's symbol."""
        matrix = self.board.matrix

        # diagonal from top left to bottom right
        diagonal_one = [matrix[offset][offset] for offset in range(3)]
        # diagonal from top right to bottom left
        diagonal_two = [matrix[offset][-offset - 1] for offset in range(3)]

        for diagonal in [diagonal_one, diagonal_two]:
            if len(set(diagonal)) == 1 and not diagonal.count(" "):
                return True
        return False

    # TODO: What if the board is full and there is no winner?


    class Player:
        """Players in Tic-Tac-Toe."""
        def __init__(self, name, symbol):
            self.name = name
            self.symbol = symbol

        def mark(self, board, x_coor, y_coor):
            """Mark own symbol on the board with given coordinate."""
            board.matrix[x_coor][y_coor] = self.symbol


    class GameBoard:
        """Game board used in Tic-Tac-Toe."""
        def __init__(self):
            self.matrix = [[" ", " ", " "] for _ in range(3)]

        def __str__(self):
            return "\n".join(str(row) for row in self.matrix)


# Main driver script
game = TicTacToe()
# game.run()
