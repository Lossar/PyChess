from chesspiece import Pawn

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
            self.board[1][i] = Pawn('p', 'w')
            self.board[6][i] = Pawn('p', 'b')

    def print_board(self):
        for x in range(len(self.board[0])):
            for y in range(len(self.board[x])):
                tile_as_text = "[    ]"
                if self.board[x][y] is not None:
                    piece = self.board[x][y]
                    tile_as_text = "[ " + piece.team_color.value + piece.piece_type + " ]"
                print(tile_as_text, " ", end="")
            print()

    def move_is_unobstructed(self, target_x, target_y, piece):
        if self.board[target_x][target_y] is not None:
            return piece.team_color == self.board[target_x][target_x]
        else:
            return True

    # Attempts to move a piece on the board. Returns true if move was a success, otherwise returns false
    def attempt_move(self, init_x, init_y, target_x, target_y):
        valid = False
        if init_x == target_x and init_y == target_y:
            print("Piece cannot move to itself")
            # Check that the provided coordinates contains a piece
        elif self.board[init_x][init_y] is not None:
            piece = self.board[init_x][init_y]
            # Check that the move conforms to the rules of movement for the piece
            if piece.move_is_valid(init_x, init_y, target_x, target_y) and self.move_is_unobstructed(target_x, target_y,piece):
                print("Move was valid")
                self.move_piece(init_x, init_y, target_x, target_y, piece)
                valid = True
            else:
                print("Move was not valid with the rules of the piece")
        return valid

    # Performs the move operation
    def move_piece(self, init_x, init_y, target_x, target_y, piece):
        self.board[target_x][target_y] = piece
        self.board[init_x][init_y] = None
        print("Piece moved")
