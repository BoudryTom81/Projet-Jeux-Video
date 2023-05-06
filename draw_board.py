"""tkinter: interface graphique """
import tkinter as tk
from PIL import Image, ImageTk


def draw_board(self):
    """dessine plateau et pions"""
    for i in range(10):
        for j in range(10):
            if (i+j)%2 == 0:
                color = "black"
            else:
                color = "pink"
            self.canvas.create_rectangle(i*self.size,
                                         j*self.size,
                                         (i+1)*self.size,
                                         (j+1)*self.size,
                                         fill=color)

    for pion in self.pions:
        if pion.couleur == self.turn:
            xptdr_a, yptdr_a = pion.position
            self.canvas.create_image(xptdr_a*self.size+self.size/2,
                                     yptdr_a*self.size+self.size/2,
                                     image=self.images[pion.image])
            # dessiner les pions adverses sur la même ligne ou colonne que le pion en cours
            for adversaire in self.pions:
                if adversaire.couleur != pion.couleur \
                        and (adversaire.position[0] == xptdr_a
                             or adversaire.position[1] == yptdr_a):
                    self.canvas.create_image(adversaire.position[0]*self.size+self.size/2,
                                             adversaire.position[1]*self.size+self.size/2,
                                             image=self.images[adversaire.image])
