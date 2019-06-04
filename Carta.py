from random import sample


class Carta:

    rangos = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

    rango_valores = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11,
                  'A': 12}

    pintas = {
        0: '\u2663',  # Clubs
        1: '\u2666',  # Diamonds
        2: '\u2665',  # Hearts
        3: '\u2660'  # Spades
    }

    valor_pinta = {
        '\u2663': 0,  # Clubs
        '\u2666': 1,  # Diamonds
        '\u2665': 2,  # Hearts
        '\u2660': 3  # Spades
    }

    def __init__(self, *args):
        if len(args) == 1:
            if args[0] not in range(54):
                raise ValueError("Id entre 0 y 54")
            self.id = args[0]
        elif len(args) == 2:
            if args[0] not in Carta.rango_valores or args[1] not in Carta.valor_pinta:
                raise ValueError("Carta Invalida")
            r = Carta.rango_valores[args[0]]
            q = Carta.valor_pinta[args[1]]

            self.id = (13 * q) + r
        else:
            raise Exception("id o pinta")

    def rango(self):
        return self.id % 13

    def pinta(self):
        return self.id // 13

    def puntos(self):
        if 9 <= self.rango() <= 12:
            return self.rango() - 8
        else:
            return 0

    def __repr__(self):
        return "{}{}".format(Carta.rangos[self.rango()], Carta.pintas[self.pinta()])

    def __lt__(self, other):
        return self.id < other.id


class CartaBlackJack(Carta):

    def puntos(self):
        if self.rango() == 12:
            return 11
        if 9 <= self.rango() <= 11:
            return 10
        else:
            return Carta.rangos[self.rango()]

    def __lt__(self, other):
        return self.rango() < other.rango()


def puntos(li):
    return sum([i.puntos() for i in li])


def new_deck(type=Carta):
    return [type(i) for i in range(52)]