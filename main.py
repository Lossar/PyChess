# This is a sample Python script.
from board import ChessBoard
from textui import TextUi

def move_and_update(init_x, init_y, target_x, target_y):
    chessboard.attempt_move(init_x, init_y, target_x, target_y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chessboard = ChessBoard()
    textui = TextUi(chessboard)
    running = True
    white_turn = True

    while running:
        print("Player", "{},".format("White" if white_turn else "Black"), "please pick a piece")
        piece = input()
        validMove = True #TODO implement actual check of valid moves

        if validMove:
            #TODO Do move
            print("Move happens here")
            white_turn = not white_turn
        else:
            print("Move was invalid here")
            #TODO retry move