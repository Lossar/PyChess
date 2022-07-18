# This is a sample Python script.
from board import ChessBoard
from textui import TextUi
from gamemanager import GameManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chessboard = ChessBoard()
    textUi = TextUi()
    gameManager = GameManager(ui=textUi, chessboard=chessboard)
    running = True
    white_turn = True

    while running:
        gameManager.run()
