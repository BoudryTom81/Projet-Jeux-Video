"""tkinter: interface graphique """
import tkinter as tk
from PIL import Image, ImageTk
from pion import FakePion



class Board(tk.Frame):
    """Board : representre le tableau de jeux"""
    def __init__(self,
                 parent,
                 size=64):
        super().__init__(parent)
        self.size = size
        self.turn = "blanc"
        self.pions = [Pion("blanc",
                           [1, 1],
                           "blanc"),
                      Pion("noir",
                           [8, 8],
                           "noir")]
        self.create_board()
