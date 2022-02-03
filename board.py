from chesspiece import ChessPiece

num_to_char = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h"
}

class ChessBoard:
    def __init__(self):
        self.board = [[None for i in range(8)] for i in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for i in range(8):
            # Make sure to change this when the time comes
            self.board[1][i] = ChessPiece('p', 'w')
            self.board[6][i] = ChessPiece('p', 'b')

    def print_board(self):
        for x in range(len(self.board[0])):
            for y in range(len(self.board[x])):
                tile_as_text = "[    ]"
                if self.board[x][y] is not None:
                    piece = self.board[x][y]
                    tile_as_text = "[ " + piece.team_color.value + piece.piece_type + " ]"
                print(tile_as_text, " ", end="")
            print()

    def move_piece(self, init_x, init_y, goal_x, goal_y):
        if self.board[init_x][init_y] is not None:
            piece = self.board[init_x][init_y]
            self.board[goal_x][goal_y] = piece
            self.board[init_x][init_y] = None
