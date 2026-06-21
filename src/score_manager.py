# score_manager.py
# Este archivo se encarga de llevar el marcador del juego.

def crear_marcador():
    """
    Crea un marcador nuevo en cero.
    Retorna un diccionario con los contadores.
    """
    marcador = {
        "victorias": 0,
        "derrotas": 0,
        "empates": 0
    }
    return marcador


def actualizar_marcador(marcador, resultado):
    """
    Actualiza el marcador según el resultado de la ronda.
    resultado puede ser: "victoria", "derrota" o "empate"
    """
    if resultado == "victoria":
        marcador["victorias"] = marcador["victorias"] + 1
    elif resultado == "derrota":
        marcador["derrotas"] = marcador["derrotas"] + 1
    else:
        marcador["empates"] = marcador["empates"] + 1

    return marcador