from tkinter import *
from random import randint


class Sello_Carta(Label):

    def __init__(self, patron):
        Label.__init__(self, patron, image=Sello_Carta.back_image)

    directorio_imagenes = './imagenes/'

    @staticmethod
    def load_images():
        Sello_Carta.images = [PhotoImage(file=Sello_Carta.directorio_imagenes + "card{}.gif".format(i)) for i in range(52)]
        Sello_Carta.back_image = PhotoImage(file=Sello_Carta.directorio_imagenes + "back-blue.gif")
        Sello_Carta.blank_image = PhotoImage(file=Sello_Carta.directorio_imagenes + "blank.gif")

    def display(self, lado='back', id=0):
        if lado == 'back':
            self.configure(image=Sello_Carta.back_image)
        elif lado == 'front':
            self.configure(image=Sello_Carta.images[id])
        else:
            self.configure(image=Sello_Carta.blank_image)