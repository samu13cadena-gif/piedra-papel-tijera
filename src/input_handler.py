# input_handler.py
# Este archivo captura y valida la jugada que escribe el usuario.

from constants import OPCIONES_VALIDAS, MENSAJE_ENTRADA_INVALIDA


def pedir_jugada_usuario():
    """
    Pide al usuario que escriba su jugada.
    Si la entrada no es válida, vuelve a preguntar (bucle de revalidación).
    """
    jugada = input("Escribe tu jugada (piedra, papel o tijera): ").lower()

    # Mientras la entrada no esté en la lista de opciones válidas, se repite la pregunta
    while jugada not in OPCIONES_VALIDAS:
        print(MENSAJE_ENTRADA_INVALIDA)
        jugada = input("Escribe tu jugada (piedra, papel o tijera): ").lower()

    return jugada