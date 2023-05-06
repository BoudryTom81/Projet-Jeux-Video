import unittest
from tkinter import Tk
from main import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.board = Board(self.root)

    def test_draw_board(self):
        # Appelle la méthode draw_board
        self.board.draw_board()
        # Compare le nombre de rectangles créés
        self.assertEqual(len(self.board.canvas.find_withtag("rectangle")), 0)
        # Compare le nombre d'images créées
        self.assertEqual(len(self.board.canvas.find_withtag("image")), 0)

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
