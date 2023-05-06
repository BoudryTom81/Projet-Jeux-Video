# Test
## Code de test
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

## sortie
C:\Users\tipil\ProjectJVBoudry_Tom\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/tipil/ProjectJVBoudry_Tom/test_create_board.py
Testing started at 16:08 ...
Launching pytest with arguments C:/Users/tipil/ProjectJVBoudry_Tom/test_create_board.py --no-header --no-summary -q in C:\Users\tipil\ProjectJVBoudry_Tom

============================= test session starts =============================
collecting ... collected 1 item

test_create_board.py::TestCreateBoard::test_create_board 

============================== 1 passed in 0.22s ==============================

Process finished with exit code 0
PASSED          [100%]
## outils
J'ai utilisé la librairie unitest pour réaliser le test de ma class Pion ainsi que chat gpt pour gagner du temps en lui demandant d'arranger ma class pour permettre de la tester.