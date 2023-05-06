# Test
## Code de test
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

## sortie
C:\Users\tipil\ProjectJVBoudry_Tom\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/tipil/ProjectJVBoudry_Tom/Test_board.py
Testing started at 14:21 ...
Launching pytest with arguments C:/Users/tipil/ProjectJVBoudry_Tom/Test_board.py --no-header --no-summary -q in C:\Users\tipil\ProjectJVBoudry_Tom

============================= test session starts =============================
collecting ... collected 1 item

Test_board.py::TestBoard::test_create_board 

============================== 1 passed in 0.22s ==============================

Process finished with exit code 0
PASSED                       [100%]                          [ 33%]PASSED                                [ 66%]PASSED                             [100%]
## outils
J'ai utilisé la librairie unitest pour réaliser le test de ma class Pion ainsi que chat gpt pour gagner du temps en lui demandant d'arranger ma class pour permettre de la tester.