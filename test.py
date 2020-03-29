import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from xo import Board, Model, Piece, print_history, play_to_completion

board = play_to_completion(Model.create(), Board.create())
print_history(board)
