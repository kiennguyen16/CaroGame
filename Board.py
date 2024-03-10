class Board:
    def __init__(self):
        self.board = [["_","_","_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]
    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
