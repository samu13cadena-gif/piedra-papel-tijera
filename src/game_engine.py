from constants import VICTORIAS_PARA_GANAR
from ui import mostrar_bienvenida, mostrar_despedida
from input_handler import pedir_jugada_usuario
from cpu_player import generar_jugada_cpu
from rules import determinar_resultado
from score_manager import crear_marcador, actualizar_marcador
from display import mostrar_resultado_ronda


def iniciar_juego():
    mostrar_bienvenida()
    marcador = crear_marcador()

    while marcador["victorias"] < VICTORIAS_PARA_GANAR and marcador["derrotas"] < VICTORIAS_PARA_GANAR:
        jugada_usuario = pedir_jugada_usuario()
        jugada_cpu = generar_jugada_cpu()
        resultado = determinar_resultado(jugada_usuario, jugada_cpu)
        marcador = actualizar_marcador(marcador, resultado)
        mostrar_resultado_ronda(jugada_usuario, jugada_cpu, resultado, marcador)

    mostrar_despedida(marcador)