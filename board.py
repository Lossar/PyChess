from chesspiece import piece_types, ChessPiece

class Tile:
    def __init__(self,):
        self.piece = None

    def set_piece(self, piece):
        self.piece = piece

class ChessBoard:
    def __init__(self):
        print("Hello world")
        self.board = [[" " for i in range(8)] for i in range(8)]

    def initialize_board(self):
        for x in range(len(self.board[0])-1):
            for y in range(len(self.board[1])-1):
                self.board[x][y] = Tile()