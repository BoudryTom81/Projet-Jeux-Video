import unittest
import tkinter as tk
from main import Board


class TestCreateBoard(unittest.TestCase):

    def test_create_board(self):
        root = tk.Tk()
        board = Board(root)
        self.assertEqual(board.size, 64)
        self.assertEqual(board.turn, "blanc")
        self.assertEqual(len(board.pions), 2)
        self.assertEqual(board.pions[0].couleur, "blanc")
        self.assertEqual(board.pions[0].position, [1, 1])
        self.assertEqual(board.pions[0].image, "blanc")
        self.assertEqual(board.pions[1].couleur, "noir")
        self.assertEqual(board.pions[1].position, [8, 8])
        self.assertEqual(board.pions[1].image, "noir")
        self.assertIsInstance(board.canvas, tk.Canvas)
        self.assertIsInstance(board.images, dict)
