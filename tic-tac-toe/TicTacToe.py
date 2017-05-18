class TicTacToe:
    board = []

    # Define your WIN_COMBINATIONS constant
    WIN_COMBINATIONS = [
        #horizonal rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        #vertical rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        #diagonals
        [0, 4, 8], [2, 4, 6]
    ]

    def __init__(self):
        self.board = [" " for index in range(9)]

    @staticmethod
    def greet():
        print("Welcome to Tic Tac Toe!")

    def show_board(self):
        print(" {} | {} | {}".format(self.board[0], self.board[1], self.board[2]))
        print("-" * 11)
        print(" {} | {} | {}".format(self.board[3], self.board[4], self.board[5]))
        print("-" * 11)
        print(" {} | {} | {}".format(self.board[6], self.board[7], self.board[8]))

    @staticmethod
    def input_to_index(user_input):
        return int(user_input - 1)

    def move(self, index, current_player="X"):
        self.board[index] = current_player

    def position_taken(self, index):
        return self.board[index] is None or self.board[index] != " "

    def valid_move(self, index):
        return index in range(0, 9) and not self.position_taken(index)

    def turn(self):
        index = int(input("Please enter 1-9: "))
        index = self.input_to_index(index)
        if self.valid_move(index):
            self.move(index, self.current_player())
            self.show_board()
        else:
            self.turn()

    def turn_count(self):
        count = 0
        for space in self.board:
            if space == "X" or space == "O":
                count += 1
        return count

    def current_player(self):
        return "X" if self.turn_count() % 2 == 0 else "O"

    def won(self):
        for win_combo in self.WIN_COMBINATIONS:
            if (self.board[win_combo[0]] == self.board[win_combo[1]] and
                    self.board[win_combo[1]] == self.board[win_combo[2]] and
                    self.position_taken(win_combo[0])):
                return win_combo
        return None

    def full(self):
        return all(space != " " for space in self.board)

    def draw(self):
        return not self.won() and self.full()

    def over(self):
        return self.full() or self.won()

    def winner(self):
        won = self.won()
        if won != None:
            return self.board[won[0]]

    def play(self):
        self.greet()
        self.show_board()
        while not self.over():
            self.turn()

            if self.draw():
                print("Cat's Game!")
            elif self.won():
                print("Congratulations {}!".format(self.winner()))
