

class GameManager:
    chessboard_ = None
    white_turn = True

    def __init__(self, ui, chessboard, audio):
        self.chessboard_ = chessboard
        self.ui = ui
        return

    def run(self):
        self.ui.on_board_update(self.chessboard_)

        chosen_piece = None
        while chosen_piece is None:
            chosen_piece = self.ui.receive_input(self.white_turn)

        if True:
            print("Move happens here")
            self.white_turn = not self.white_turn
        else:
            print("Move was invalid here")

    def move_and_update(self, init_x, init_y, target_x, target_y):
        self.chessboard_.attempt_move(init_x, init_y, target_x, target_y)

    def on_move_piece(self):
        self.move_and_update()
        return

    def on_remove_piece(self):
        return

    def on_game_over(self):
        return
