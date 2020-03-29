from xo.model import Model
from xo.state import Board, Piece


def get_optimal_move(model, board):
    blank_indices = board.get_indices_of_blanks()

    # work out which player!
    move_scores = {
        i: model.predict(board.play(i).to_nn_input())
        for i in blank_indices
    }

    return max(move_scores, key=move_scores.get)


def play_to_completion(model, board=Board.create()):
    while not board.is_game_over():
        move = get_optimal_move(model, board)
        board = board.play(move)

    return board
