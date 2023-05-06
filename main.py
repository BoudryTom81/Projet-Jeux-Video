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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pions")
    game = Board(root)
    game.pack(side="top",
              fill="both",
              expand=True)
    root.mainloop()
