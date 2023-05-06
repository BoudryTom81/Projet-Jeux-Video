# Test
## Code de test
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

## sortie
C:\Users\tipil\ProjectJVBoudry_Tom\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/tipil/ProjectJVBoudry_Tom/test_draw_board.py
Testing started at 16:50 ...
Launching pytest with arguments C:/Users/tipil/ProjectJVBoudry_Tom/test_draw_board.py --no-header --no-summary -q in C:\Users\tipil\ProjectJVBoudry_Tom

============================= test session starts =============================
collecting ... collected 1 item

test_draw_board.py::TestBoard::test_draw_board 

============================== 1 passed in 0.25s ==============================

Process finished with exit code 0
PASSED                    [100%]
## outils
J'ai utilisé la librairie unitest pour réaliser le test de ma class Pion ainsi que chat gpt pour gagner du temps en lui demandant d'arranger ma class pour permettre de la tester.