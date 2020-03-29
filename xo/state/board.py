from __future__ import annotations
from enum import Enum
from typing import List, Optional
import tensorflow as tf


class Piece(Enum):
    BLANK = 0
    NOUGHT = 1
    CROSS = 2

    def invert(self) -> Piece:
        if self == Piece.CROSS:
            return Piece.NOUGHT

        if self == Piece.NOUGHT:
            return Piece.CROSS

        raise ValueError("cannot invert blank piece")


class Board:
    SIZE = 9
    ROW_LENGTH = 3

    def __init__(
        self, board_positions, previous=None, next_player=Piece.CROSS
    ):
        self._array = board_positions
        self.previous = previous
        self._next_player = next_player

    @staticmethod
    def create() -> Board:
        return Board([Piece.BLANK for _ in range(Board.SIZE)])

    def set(self, index_to_set: int, new_value: Piece) -> Board:
        return Board(
            [
                new_value if index == index_to_set else old_value
                for index, old_value in enumerate(self._array)
            ],
            self,
        )

    def play(self, at_index: int) -> Board:
        if self._array[at_index] != Piece.BLANK:
            raise RuntimeError("cannot play on taken space")

        board = self.set(at_index, self._next_player)
        self._next_player = self._next_player.invert()
        return board

    def to_array(self) -> List[Piece]:
        return self._array

    def get_indices_of_blanks(self) -> List[int]:
        return [i for i, p in enumerate(self._array) if p == Piece.BLANK]

    def to_nn_input(self) -> List[int]:
        us = [p == self._next_player for p in self._array]
        them = [p == self._next_player.invert() for p in self._array]
        return tf.constant(us + them, shape=(1, 18))

    def has_winner(self) -> bool:
        return bool(self.get_winning_player())

    def is_full(self) -> bool:
        return all([p != Piece.BLANK for p in self._array])

    def is_game_over(self) -> bool:
        return self.has_winner() or self.is_full()

    @staticmethod
    def _get_winner_for_run(run: List[Piece]) -> Optional[Piece]:
        first_piece = run[0]

        if first_piece == Piece.BLANK:
            return None

        if all(map(lambda p: p == first_piece, run)):
            return first_piece

        return None

    def _run_indices_to_pieces(self, run: List[int]) -> List[Piece]:
        return [self._array[i] for i in run]

    def get_winning_player(self) -> Optional[Piece]:
        runs = (
            # horizontals
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            # verticals
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            # diagonals
            [0, 4, 8],
            [2, 4, 6],
        )

        for run in map(self._run_indices_to_pieces, runs):
            winning_piece = self._get_winner_for_run(run)

            if winning_piece:
                return winning_piece

        return None
