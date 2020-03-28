from xo import Board, Piece, print_board

board = Board.fresh()
board = board.set(2, Piece.CROSS)
board = board.set(3, Piece.NOUGHT)

print_board(board)
