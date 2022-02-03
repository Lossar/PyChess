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
