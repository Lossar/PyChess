class TextUi:

    def print_board(self, chessboard):
        for x in range(len(chessboard.board[0])):
            for y in range(len(chessboard.board[x])):
                tile_as_text = "[    ]"
                if chessboard.board[x][y] is not None:
                    piece = chessboard.board[x][y]
                    tile_as_text = "[ " + piece.team_color.value + piece.piece_type + " ]"
                print(tile_as_text, " ", end="")
            print()

    def on_board_update(self, chessboard):
        self.print_board(chessboard)

    def receive_input(self, white_turn):
        print("Player", "{},".format("White" if white_turn else "Black"), "please pick a piece")
        piece = input()
        return piece if self.is_valid_input(piece) else None

    def is_valid_input(self, input_string):
        return len(input_string) == 2 and input_string[1].isnumeric()
