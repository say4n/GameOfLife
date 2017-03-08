import unittest

from game_of_life.board import *
from game_params.game_params import *

class TestBoard(unittest.TestCase):

    def test_step(self):        
        b = Board(5, 5 , [[1,2], [2,2], [3,2]])
        b.step()

        self.assertEqual(b.board[3][2], 0)
        self.assertEqual(b.board[2][2], 1)
        self.assertEqual(b.board[2][3], 1)
        self.assertEqual(b.board[1][2], 0)
        self.assertEqual(b.board[2][1], 1)

    def test_step(self):

        b = Board(1, 1, [[0,0]])
        b.step()

        self.assertEqual(b.board[0][0], 0)

    def test_board_none_dim(self):
        self.assertRaises(TypeError, Board, None, None)

    def test_negative_alive_point(self):

        self.assertRaises(IndexError, Board, 5, 5, [[-10,-5]])

    def test_out_of_bound_alive_point(self):
        self.assertRaises(IndexError, Board, 5, 5, [[20,20]])


    def test_dimension_error(self):
        self.assertRaises(ValueError, Board, -1, -1)

    def test_show(self):

        b = Board(1, 1, [[0,0]])
        self.assertEqual(str(b), u"{}\n".format(live_marker))


if __name__ == '__main__':
    unittest.main()