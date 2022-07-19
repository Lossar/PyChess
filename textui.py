from CharToNum import char_to_num, num_to_char

class TextUi:
    x_y_limit = 7

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


    def prompt_pick_piece(self, white_turn):
        print("Player", "{},".format("White" if white_turn else "Black"), "please pick a piece")


    def prompt_pick_target(self, white_turn):
        print("Player", "{},".format("White" if white_turn else "Black"), "please pick a target")

    def inform_invalid_move(self, x, y, target_x, target_y):
        print("Move was invalid! Piece at {}{} could not reach target {}{}"
              .format(num_to_char[x], y, num_to_char[target_x], target_y))

    def receive_input(self):
        input_coord = input().lower()

        return [char_to_num[input_coord[0]], int(input_coord[1]) - 1] if self.is_valid_input(input_coord) else [None, None]

    def is_valid_input(self, input_coord):
        if self.is_input_valid_lenght(input_coord) is False:
            print("Input is not correct length! correct length is 2")
            return False

        x, y = input_coord[0], int(input_coord[1])

        if self.is_x_valid(x) is False:
            print("X of value {} is invalid! Only letters a through h are valid".format(x))
            return False
        else:
            x = char_to_num[x]

        if self.is_y_valid(y) is False:
            print("Y is invalid!")
            return False

        return True

    def is_y_valid(self, y):
        return 1 <= y <= self.x_y_limit

    def is_x_valid(self, x):
        return 97 <= ord(x) <= 103

    def is_input_valid_lenght(self, input_coord):
        return len(input_coord) == 2
