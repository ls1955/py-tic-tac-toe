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
            print(f"Please choose x coordinate, {self.curr_player().name}")
            counter -= 1

    def curr_player(self):
        """Return current player object for every turn."""
        return self.player_one if self.is_player_one_turn else self.player_two

    # def is_valid(coor)

    # def has_horizontal_winner(coor)

    # def has_vertical_winner(coor)

    # def has_diagonal_winner(coor)


    class Player:
        """Players in Tic-Tac-Toe."""
        def __init__(self, name, symbol):
            self.name = name
            self.symbol = symbol
    
    class GameBoard:
        """Game board used in Tic-Tac-Toe."""
        def __init__(self):
            self.board = [[[" "] for _ in range(3)] for _ in range(3)]
        
        # TODO: Implement #to_string so it could print nicely on terminal

# Main driver script
game = TicTacToe()
game.run()
