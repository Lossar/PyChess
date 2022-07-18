class GameManager:
    chessboard_ = None
    white_turn = True

    def __init__(self, ui, chessboard):
        self.chessboard_ = chessboard
        self.ui = ui

    def run(self):
        self.ui.on_board_update(self.chessboard_)
        x, y, target_y, target_x = None, None, None, None

        while x is None and y is None:
            self.ui.prompt_pick_piece(self.white_turn)
            x, y = self.ui.receive_input()

        while target_x is None and target_y is None:
            self.ui.prompt_pick_target(self.white_turn)
            target_x, target_y = self.ui.receive_input()

        if self.chessboard_.attempt_move(x, y, target_x, target_y):
            print("Move happens here")
            self.ui.on_board_update(self.chessboard_)
            self.white_turn = not self.white_turn
        else:
            print("Move was invalid! Try again")

    def move_and_update(self, init_x, init_y, target_x, target_y):
        self.chessboard_.attempt_move(init_x, init_y, target_x, target_y)

    def on_move_piece(self):
        self.move_and_update()
        return

    def on_remove_piece(self):
        return

    def on_game_over(self):
        return
