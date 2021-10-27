import unittest
from chess_game.chess_twist import ChessGame


class TestPredict(unittest.TestCase):
    def setUp(self) -> None:
        self.chess_board = ChessGame(origin={'x': -1, 'y': 1})
        self.instructions = 'd1,r1'

    def test_check_origin(self):
        assert self.chess_board.current_x == -1
        assert self.chess_board.current_y == 1

    def test_move_rook(self):
        self.chess_board.move_series(self.instructions)
        self.assertEqual(self.chess_board.current_y, 0)
        self.assertEqual(self.chess_board.current_x, 0)
        self.assertEqual(self.chess_board.total_spaces_moved, 2)
        self.assertEqual(self.chess_board.spaces_from_start, 2)

    def test_multiple_movements_results_relative_to_original_origin(self):
        """ For example second movement should update total_spaces_moved, and
        space_from_start, from original origin, not from the last position"""
        self.chess_board.move_series(self.instructions)
        self.assertEqual(self.chess_board.total_spaces_moved, 2)
        self.assertEqual(self.chess_board.spaces_from_start, 2)
        self.chess_board.move_series(self.instructions)
        self.assertEqual(self.chess_board.total_spaces_moved, 4)
        self.assertEqual(self.chess_board.spaces_from_start, 4)


if __name__ == '__main__':
    unittest.main()
