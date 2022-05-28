class TextUi:
    def __init__(self, chessboard):

        def print_board(self):
            for x in range(len(self.chessboard.board[0])):
                for y in range(len(self.chessboard.board[x])):
                    tile_as_text = "[    ]"
                    if self.chessboard.board[x][y] is not None:
                        piece = self.chessboard.board[x][y]
                        tile_as_text = "[ " + piece.team_color.value + piece.piece_type + " ]"
                    print(tile_as_text, " ", end="")
                print()
