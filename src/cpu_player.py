import random
from constants import OPCIONES_VALIDAS


def generar_jugada_cpu():
    jugada = random.choice(OPCIONES_VALIDAS)
    return jugada