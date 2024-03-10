from Board import Board

class XO:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def next_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
            print(f"Lượt của {self.current_player} ")
        else:
            self.current_player = 'X'
            print(f"Lượt của {self.current_player} ")

    def make_move(self, row, col):
        if self.board.board[row][col] == '_':
            self.board.board[row][col] = self.current_player
            self.next_player()
        else:
            print("Chọn vị trí khác")

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


    def checkFull(self):
            for row in self.board.board:
                if '_' in row:
                    return False
            return True
    def print_board(self):
        self.board.print_board()