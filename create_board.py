"""tkinter: interface graphique """
import tkinter as tk
from PIL import Image, ImageTk


def create_board(self):
    """pour creer le canvas et generer des images pour les pions"""
    self.canvas = tk.Canvas(self,
                            width=self.size*10,
                            height=self.size*10,
                            borderwidth=0,
                            highlightthickness=0)
    self.canvas.pack(side="top", fill="both",
                     expand="true")
    self.canvas.bind("<Button-1>",
                     self.move_pion)
    self.images = {
        "blanc": ImageTk.PhotoImage(Image.open("C:"
                                               "/Users"
                                               "/tipil"
                                               "/OneDrive"
                                               "/Bureau"
                                               "/Cours"
                                               "/Python"
                                               "/Pjv"
                                               "/Mickey.png").resize((self.size,
                                                self.size))),
        "noir": ImageTk.PhotoImage(Image.open("C:"
                                              "/Users"
                                              "/tipil"
                                              "/OneDrive"
                                              "/Bureau"
                                              "/Cours"
                                              "/Python"
                                              "/Pjv"
                                              "/Bob.png").resize((self.size,
                                                self.size)))
    }
    self.draw_board()
