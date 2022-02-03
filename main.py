# This is a sample Python script.
from board import ChessBoard


def move_and_update(init_x, init_y, target_x, target_y):
    chessboard.attempt_move(init_x, init_y, target_x, target_y)
    chessboard.print_board()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chessboard = ChessBoard()
    move_and_update(1, 1, 1, 2)
    move_and_update(1, 1, 2, 1)
    move_and_update(1, 1, 1, 1)
    move_and_update(2, 1, 4, 1)

    running = True
    white_turn = True

    while running:
        print("Player ", "White" if white_turn else "Black", " Please pick a piece")
        piece = input()