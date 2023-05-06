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
