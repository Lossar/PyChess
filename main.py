# This is a sample Python script.
from board import ChessBoard

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chessboard = ChessBoard()
    chessboard.print_board()

    running = True
    white_turn = True
    while running:
        print("Player ", "White" if white_turn else "Black", " Please pick a piece")
        piece = input()