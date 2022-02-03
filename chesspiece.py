from enum import Enum


class Color(Enum):
    WHITE = "W"
    BLACK = "B"


class ChessPiece:
    def __init__(self, piece_type, team_color):
        self.piece_types = ['p']

        if piece_type in self.piece_types:
            self.piece_type = piece_type
        else:
            raise ValueError("Piece was defined with invalid type")

        if team_color == 'w':
            self.team_color = Color.WHITE
        elif team_color == 'b':
            self.team_color = Color.BLACK
        else:
            raise ValueError("Chess pieces must belong to either the white or black team")

    def move_is_valid(self, self_x, self_y, x, y):
        raise NotImplementedError("Please implement this in child classes")


class Pawn(ChessPiece):
    def __init__(self, piece_type, team_color):
        super(Pawn, self).__init__(piece_type, team_color)

    def move_is_valid(self, self_x, self_y, x, y):
        valid = True
        if abs(self_x - x) > 1 or abs(self_y - y) > 1:
            valid = False
        return valid
