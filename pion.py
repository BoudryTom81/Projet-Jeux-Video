"""tkinter: interface graphique """
import tkinter as tk
from PIL import Image, ImageTk


class Pion:
    """la classe pour presenter pions"""
    def __init__(self,
                 couleur,
                 position,
                 image):
        self.couleur = couleur
        self.position = position
        self.image = image
