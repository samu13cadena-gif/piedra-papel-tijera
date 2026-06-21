# cpu_player.py
# Este archivo genera la jugada de la computadora de forma aleatoria.

import random
from constants import OPCIONES_VALIDAS


def generar_jugada_cpu():
    """
    Elige una opción al azar entre piedra, papel o tijera.
    Cada opción tiene la misma probabilidad de salir (1/3).
    """
    jugada = random.choice(OPCIONES_VALIDAS)
    return jugada