from tkinter.messagebox import showinfo
from Sello_Carta import *
from Baraja import *


baraja = Baraja(CartaBlackJack)


dealer = []
jugador = []


dgana_puntaje = 0
pgana_puntaje = 0



def reiniciar():
    global dealer, jugador

    baraja.rebarajar(dealer)
    dealer = []
    baraja.rebarajar(jugador)
    jugador = []

    for carta in range(6):
        dealer_sello[carta].display('blank')
        jugador_sello[carta].display('blank')


def nuevo_juego():
    boton_pedir.config(state='disabled')
    boton_pasar.config(state='disabled')
    boton_repartir.config(state='normal')


def dealergana():
    global dgana_puntaje
    showinfo(message='Perdió.')
    nuevo_juego()
    dgana_puntaje += 1
    dealer_gana.config(text='Dealer gana: {}'.format(dgana_puntaje))


def jugadorgana():
    global pgana_puntaje
    showinfo(message='Ganador!')
    nuevo_juego()
    pgana_puntaje += 1
    jugador_gana.config(text='Jugador Gana: {}'.format(pgana_puntaje))


def juegoempatado():
    showinfo(message='Empate!')
    nuevo_juego()


def total(mano):
    num_ases = 0

    resultado = puntos(mano)

    for carta in mano:
        if carta.rango() == 12:
            num_ases += 1


    while resultado > 21 and num_ases > 0:
        resultado -= 10
        num_ases -= 1

    return resultado


def debug():
    print("Mano del dealer =", dealer)
    print("Mano del jugador =", jugador)
    print("Puntaje Dealer =", total(dealer))
    print("Puntaje Jugador=", total(jugador))


def pedir():
    global dealer, jugador

    reiniciar()
    baraja.shuffle()

    dealer += baraja.pedir(2)
    jugador += baraja.pedir(2)

    dealer_sello[0].display('back', dealer[0].id)
    dealer_sello[1].display('front', dealer[1].id)
    jugador_sello[0].display('front', jugador[0].id)
    jugador_sello[1].display('front', jugador[1].id)

    boton_pedir.config(state='normal')
    boton_pasar.config(state='normal')
    boton_repartir.config(state='disabled')

    if total(jugador) == 21:
        jugadorgana()

    elif total(dealer) == 21:
        dealergana()




def otra():

    global jugador

    indice_cartas = len(jugador)

    jugador += baraja.pedir(1)

    jugador_sello[indice_cartas].display('front', jugador[-1].id)

    if total(jugador) > 21:
        dealergana()

    elif total(jugador) == 21:
        jugadorgana()

def pasar_carta():

    global dealer, jugador

    dealer_sello[0].display('front', dealer[0].id)

    while total(dealer) < 17:
        indice_cartas = len(dealer)
        dealer += baraja.pedir(1)
        dealer_sello[indice_cartas].display('front', dealer[-1].id)

    if total(dealer) > 21:
        jugadorgana()

    elif total(dealer) > total(jugador):
        dealergana()

    elif total(dealer) < total(jugador):
        jugadorgana()

    elif total(dealer) == total(jugador):
        juegoempatado()


root = Tk()
Sello_Carta.load_images()


dealer_sello = [0] * 6
jugador_sello = [0] * 6

for carta in range(6):

    dealer_sello[carta] = Sello_Carta(root)
    dealer_sello[carta].grid(row=0, column=carta, padx=10, pady=10)
    dealer_sello[carta].display('blank')


    jugador_sello[carta] = Sello_Carta(root)
    jugador_sello[carta].grid(row=1, column=carta, padx=10, pady=10)
    jugador_sello[carta].display('blank')


dealer_gana = Label(root, text='Dealer\'s score:  ')
dealer_gana.grid(row=0, column=6, sticky=W, padx=20, pady=10)

jugador_gana = Label(root, text='Player\'s score:  ')
jugador_gana.grid(row=1, column=6, sticky=W, padx=20, pady=10)


boton_repartir = Button(root, text='Repartir', command=pedir)
boton_repartir.grid(row=2, column=0, columnspan=2, pady=10)

boton_pedir = Button(root, text='Pedir', state='disabled', command=otra)
boton_pedir.grid(row=2, column=2, columnspan=2, pady=10)

boton_pasar = Button(root, text='Pasar', state='disabled', command=pasar_carta)
boton_pasar.grid(row=2, column=4, columnspan=2, pady=10)


root.rowconfigure(0, minsize=115)
root.columnconfigure(0, minsize=85)

if __name__ == '__main__':
    root.mainloop()
