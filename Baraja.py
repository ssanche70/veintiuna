"""
Deck.py: Assignment 2.2, CIS 211
Author: Momo Ozawa

This program contains the definitions for a class Deck that represents a deck of playing cards, and
a class PinochleDeck that inherits methods from Card.
"""
from Carta import *
from random import shuffle


class Baraja(list):

    def __init__(self, cls=Carta):
        list.__init__(self, [cls(i) for i in range(52)])

    def shuffle(self):
        shuffle(self)

    def pedir(self, *args):

        if len(args) == 1 and isinstance(args[0], int):
            num_cartas = args[0]
            return [self.pop(0) for i in range(num_cartas)]
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            num_cartas = args[0]
            num_manos = args[1]
            manos = [ ]


            for mano in range(num_manos):
                manos.append([ ])


            for carta in range(num_cartas):
                for mano in range(num_manos):
                    manos[mano].append(self.pop(0))

            return manos
        else:
            raise ValueError("pedir() solamente maneja dos enteros")

    def rebarajar(self, a):

        for elemento in a:
            if not isinstance(elemento, Carta):
                raise ValueError("Solamente podemos regresar las cartas existantes.")
        self += a

    def append(self, carta):
        if not isinstance(carta, Carta):
            raise ValueError("Solamente se pueden agregar cartas.")
        self.append(carta)


class Pinochlebaraja(Baraja):

    def __init__(self):

        p_baraja = []

        for i in range(52):
            if i % 13 >= 7:
                p_baraja.append(Carta(i))
                p_baraja.append(Carta(i))

        list.__init__(self, p_baraja)
