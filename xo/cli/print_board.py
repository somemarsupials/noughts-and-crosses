from textwrap import indent
from typing import List

from xo.state import Board, Piece


def _piece_to_string(piece: Piece) -> str:
    if piece == Piece.CROSS:
        return "x"

    if piece == Piece.NOUGHT:
        return "o"

    return " "


def _row_to_string(row: List[Piece]) -> str:
    return " | ".join(map(_piece_to_string, row))


def _board_to_rows(board: Board) -> List[List[Piece]]:
    array = board.to_array()
    return [
        array[i : i + Board.ROW_LENGTH]
        for i in range(0, Board.SIZE, Board.ROW_LENGTH)
    ]


def _board_to_string(board: Board) -> str:
    string_rows = [_row_to_string(r) for r in _board_to_rows(board)]
    return "\n{}\n".format("-" * len(string_rows[0])).join(string_rows)


def print_board(board: Board) -> None:
    print(indent(_board_to_string(board), "\t"))
