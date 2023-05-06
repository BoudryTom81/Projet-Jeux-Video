# Test
## Code de test
import unittest
from main import Board


class TestBoard(unittest.TestCase):

    def test_move_pion(self):
        # création d'un plateau de jeu
        board = Board(None)
        # on sélectionne le pion blanc en position [1, 1]
        board.pions[0].position = [1, 1]
        # on simule le déplacement du pion blanc vers la droite
        event = type("Event", (), {"x": 128, "y": 64})()
        board.move_pion(event)
        # on vérifie que le pion a bien été déplacé
        self.assertEqual(board.pions[0].position, [2, 1])

## sortie
C:\Users\tipil\ProjectJVBoudry_Tom\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/tipil/ProjectJVBoudry_Tom/test_move_pion.py
Testing started at 17:57 ...
Launching pytest with arguments C:/Users/tipil/ProjectJVBoudry_Tom/test_move_pion.py --no-header --no-summary -q in C:\Users\tipil\ProjectJVBoudry_Tom

============================= test session starts =============================
collecting ... collected 1 item

test_move_pion.py::TestBoard::test_move_pion 

============================== 1 passed in 0.24s ==============================

Process finished with exit code 0
PASSED                      [100%]
## outils
J'ai utilisé la librairie unitest pour réaliser le test de ma class Pion ainsi que chat gpt pour gagner du temps en lui demandant d'arranger ma class pour permettre de la tester.