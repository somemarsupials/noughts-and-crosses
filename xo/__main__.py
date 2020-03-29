import os
from xo import Board, Model, print_history, play_to_completion

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
print_history(play_to_completion(Model.create(), Board.create()))
