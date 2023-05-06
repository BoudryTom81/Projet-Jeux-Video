"""tkinter: interface graphique """
import tkinter as tk
from PIL import Image, ImageTk


def move_pion(self, event):
    """deplace les pions"""
    xptdr_a, yptdr_a = event.x // self.size, event.y // self.size
    for pion in self.pions:
        if pion.position == [xptdr_a, yptdr_a]:
            return
    selected_pion = None
    for pion in self.pions:
        if pion.position in (
                [xptdr_a - 2, yptdr_a],
                [xptdr_a + 2, yptdr_a],
                [xptdr_a, yptdr_a - 2],
                [xptdr_a, yptdr_a + 2],
                [xptdr_a - 1, yptdr_a],
                [xptdr_a + 1, yptdr_a],
                [xptdr_a, yptdr_a - 1],
                [xptdr_a, yptdr_a + 1]):
            if pion.couleur == self.turn:
                if selected_pion is None:
                    selected_pion = pion
                else:
                    return
    if selected_pion is not None:
        xptdr_b, yptdr_b = selected_pion.position
        if xptdr_b == xptdr_a or yptdr_b == yptdr_a:
            # Si le pion sélectionné est sur la même ligne ou colonne que la case cliquée,
            # on vérifie que l'adversaire est sur la même ligne ou colonne
            for pion in self.pions:
                if pion.couleur != self.turn:
                    xptdr_c, yptdr_c = pion.position
                    if xptdr_b == xptdr_c or yptdr_b == yptdr_c:
                        # Si l'adversaire est sur la même ligne ou colonne, on le montre
                        self.canvas.create_rectangle(xptdr_c * self.size,
                                                     yptdr_c * self.size,
                                                     (xptdr_c + 1) * self.size,
                                                     (yptdr_c + 1) * self.size,
                                                     fill="red")
                        break
        selected_pion.position = [xptdr_a, yptdr_a]
        self.turn = "blanc" if self.turn == "noir" else "noir"
        self.canvas.delete("all")
        self.draw_board()
