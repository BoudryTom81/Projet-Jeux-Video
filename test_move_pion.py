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
