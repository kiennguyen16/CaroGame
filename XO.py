from Board3x3 import Board3x3
from Board5x5 import Board5x5


class XO:
    def __init__(self):
        self.board = None
        self.current_player = 'X'

    def select_board(self):
        size = int(input("Choose 3 (3x3) or 5 (5x5): "))
        if size == 3:
            self.board = Board3x3()
            self.play3x3()
        elif size == 5:
            self.board = Board5x5()
            self.play5x5()
        else:
            print("Choose 3 or 5 only.")
            self.select_board()

    def next_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
            print(f"{self.current_player} player turn")
        else:
            self.current_player = 'X'
            print(f"{self.current_player} player turn")

    def make_move(self, row, col):
        if self.board.board[row][col] == '_':
            self.board.board[row][col] = self.current_player
            self.next_player()
        else:
            print("Choose another position")

    def check_winner(self):
        for i in range(0,3):
            if self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] and self.board.board[i][0] != '_':
                return self.board.board[i][0]
            if self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] and self.board.board[0][i] != '_':
                return self.board.board[0][i]
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] and self.board.board[0][0] != '_':
            return self.board.board[0][0]
        if self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] and self.board.board[0][2] != '_':
            return self.board.board[0][2]
        return None

    def check_winner5x5(self):
        for i in range(0, 5):
            if self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] == self.board.board[i][3] == self.board.board[i][4] and self.board.board[i][0] != '_':
                return self.board.board[i][0]
            if self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] == self.board.board[3][i] == self.board.board[4][i] and self.board.board[0][i] != '_':
                return self.board.board[0][i]
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == self.board.board[3][3] == self.board.board[4][4] and self.board.board[0][0] != '_':
            return self.board.board[0][0]
        if self.board.board[0][4] == self.board.board[1][3] == self.board.board[2][2] == self.board.board[3][1] == self.board.board[4][0] and self.board.board[0][4] != '_':
            return self.board.board[0][4]

    def checkFull(self):
        for row in self.board.board:
            if '_' in row:
                return False
        return True
    def print_board(self):
        self.board.print_board()

    def play3x3(self):
        print("Player X plays first")
        self.print_board()
        while True:
            row = -1
            col = -1
            while not 0 <= row <= 2:
                row = int(input("Choose row number from 0 to 2: "))
                if not 0 <= row <= 2:
                    print("Please input row in this range ( 0, 2 )")
            while not 0 <= col <= 2:
                col = int(input("Choose column number from 0 to 2: "))
                if not 0 <= col <= 2:
                    print("Please input column in this range ( 0, 2 )")
            self.make_move(row, col)
            self.print_board()
            if self.checkFull():
                print("DRAW")
                break
            elif self.check_winner():
                print(f"Congratulations the winner is player: {self.check_winner()}")
                break

    def play5x5(self):
        print("Player X plays first")
        self.board.print_board()
        while True:
            row = -1
            col = -1
            while not 0 <= row <= 4:
                row = int(input("Choose row number from 0 to 4: "))
                if not 0 <= row <= 4:
                    print("Please input row in this range ( 0, 4 )")
            while not 0 <= col <= 4:
                col = int(input("Choose column number from 0 to 4: "))
                if not 0 <= col <= 4:
                    print("Please input column in this range ( 0, 4 )")
            self.make_move(row, col)
            self.board.print_board()
            if self.checkFull():
                print("DRAW")
                break
            elif self.check_winner5x5():
                print(f"Congratulations the winner is player: {self.check_winner()}")
                break