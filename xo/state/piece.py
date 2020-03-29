from enum import Enum


class Piece(Enum):
    BLANK = 0
    NOUGHT = 1
    CROSS = 2

    def invert(self):
        if self == Piece.CROSS:
            return Piece.NOUGHT

        if self == Piece.NOUGHT:
            return Piece.CROSS

        raise ValueError("cannot invert blank piece")
