from __future__ import annotations
from enum import Enum


class Piece(Enum):
    BLANK = 0
    NOUGHT = 1
    CROSS = 2

    def invert(self) -> Piece:
        if self.value == Piece.CROSS:
            return Piece.NOUGHT

        if self.value == Piece.NOUGHT:
            return Piece.CROSS

        raise ValueError("cannot invert blank piece")


class Board:
    SIZE = 9
    ROW_LENGTH = 3

    def __init__(self, board_positions):
        self._array = board_positions

    @staticmethod
    def fresh() -> Board:
        return Board([Piece.BLANK for _ in range(Board.SIZE)])

    def set(self, index_to_set: int, new_value: Piece) -> Board:
        return Board(
            [
                new_value if index == index_to_set else old_value
                for index, old_value in enumerate(self._array)
            ]
        )

    def to_array(self):
        return self._array

    def has_winner(self):
        pass

    def get_winning_player(self):
        pass
