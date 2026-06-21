# game_engine.py
# Este archivo orquesta el flujo completo del juego: conecta todos los demás módulos.

from constants import VICTORIAS_PARA_GANAR
from ui import mostrar_bienvenida, mostrar_despedida
from input_handler import pedir_jugada_usuario
from cpu_player import generar_jugada_cpu
from rules import determinar_resultado
from score_manager import crear_marcador, actualizar_marcador
from display import mostrar_resultado_ronda


def iniciar_juego():
    """
    Controla el ciclo principal del juego.
    Se repite (bucle while) hasta que el usuario o la CPU lleguen a 2 victorias.
    """
    mostrar_bienvenida()
    marcador = crear_marcador()

    # Bucle principal: continúa mientras nadie haya llegado a 2 victorias
    while marcador["victorias"] < VICTORIAS_PARA_GANAR and marcador["derrotas"] < VICTORIAS_PARA_GANAR:
        jugada_usuario = pedir_jugada_usuario()
        jugada_cpu = generar_jugada_cpu()
        resultado = determinar_resultado(jugada_usuario, jugada_cpu)
        marcador = actualizar_marcador(marcador, resultado)
        mostrar_resultado_ronda(jugada_usuario, jugada_cpu, resultado, marcador)

    mostrar_despedida(marcador)