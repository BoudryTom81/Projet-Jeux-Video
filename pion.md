# Test
## Code de test
import unittest
from pion import Pion

class TestPion(unittest.TestCase):

    def setUp(self):
        self.pion_blanc = Pion('blanc', (0, 0), 'Bob.png')
        self.pion_noir = Pion('noir', (1, 1), 'Mickey.png')

    def test_couleur(self):
        self.assertEqual(self.pion_blanc.couleur, 'blanc')
        self.assertEqual(self.pion_noir.couleur, 'noir')

    def test_position(self):
        self.assertEqual(self.pion_blanc.position, (0, 0))
        self.assertEqual(self.pion_noir.position, (1, 1))

    def test_image(self):
        self.assertEqual(self.pion_blanc.image, 'Bob.png')
        self.assertEqual(self.pion_noir.image, 'Mickey.png')

if __name__ == '__main__':
    unittest.main()

## sortie
C:\Users\tipil\ProjectJVBoudry_Tom\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/tipil/ProjectJVBoudry_Tom/test_pion.py
Testing started at 22:21 ...
Launching pytest with arguments C:/Users/tipil/ProjectJVBoudry_Tom/test_pion.py --no-header --no-summary -q in C:\Users\tipil\ProjectJVBoudry_Tom

============================= test session starts =============================
collecting ... collected 3 items

test_pion.py::TestPion::test_couleur 
test_pion.py::TestPion::test_image 
test_pion.py::TestPion::test_position 

============================== 3 passed in 0.16s ==============================

Process finished with exit code 0
PASSED                              [ 33%]PASSED                                [ 66%]PASSED                             [100%]
## outils
J'ai utilisé la librairie unitest pour réaliser le test de ma class Pion ainsi que chat gpt pour gagner du temps en lui demandant d'arranger ma class pour permettre de la tester.