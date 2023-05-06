import unittest
from board import Board


class FakePion:
    def __init__(self, couleur, position, direction):
        self.couleur = couleur
        self.position = position
        self.direction = direction


class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = Board(None, size=64)
        self.assertEqual(board.size, 64)
        self.assertEqual(board.turn, "blanc")
        self.assertEqual(len(board.pions), 2)
        self.assertIsInstance(board.pions[0], FakePion)
        self.assertIsInstance(board.pions[1], FakePion)
