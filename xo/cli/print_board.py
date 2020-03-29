from textwrap import indent
from xo.state import Board, Piece


def _piece_to_string(piece):
    if piece == Piece.CROSS:
        return "x"

    if piece == Piece.NOUGHT:
        return "o"

    return " "


def _row_to_string(row):
    return " | ".join(map(_piece_to_string, row))


def _board_to_rows(board):
    array = board.to_array()

    return [
        array[i : i + Board.ROW_LENGTH]
        for i in range(0, Board.SIZE, Board.ROW_LENGTH)
    ]


def _board_to_string(board):
    string_rows = [_row_to_string(r) for r in _board_to_rows(board)]
    return "\n{}\n".format("-" * len(string_rows[0])).join(string_rows)


def print_board(board):
    print(indent(_board_to_string(board), "\t"))


def print_history(board):
    states = [board]

    while board.previous is not None:
        states.append(board.previous)
        board = board.previous

    for index, state in enumerate(reversed(states)):
        print("\n{} {}\n".format(index, "~" * 20))
        print_board(state)
