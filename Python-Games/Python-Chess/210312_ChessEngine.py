"""
https://www.youtube.com/watch?v=EnYui0e73Rs
This class is responsible for 
1.- storing all of the information about the current state of the chess game
2.- Determining the valid moves at the current state
3.- Keep a move log.
"""

class GameState():
    def __init__(self):
        # board is an 8x8 2d list and each piece is represented by a two character string
        # the first string is the color white (w) or black (b) and the second character is the piece type
        # rook R), Knight(N), Bishop(B), Queen(Q), King(K) and Pawn(p)
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []