from constants import OPCIONES_VALIDAS, MENSAJE_ENTRADA_INVALIDA


def pedir_jugada_usuario():
    jugada = input("Escribe tu jugada (piedra, papel o tijera): ").lower()

    while jugada not in OPCIONES_VALIDAS:
        print(MENSAJE_ENTRADA_INVALIDA)
        jugada = input("Escribe tu jugada (piedra, papel o tijera): ").lower()

    return jugada