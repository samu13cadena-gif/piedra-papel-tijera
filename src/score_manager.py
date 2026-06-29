# score_manager.py
# Este archivo se encarga de llevar el marcador y el historial del juego.

def crear_marcador():
    """
    Crea un marcador nuevo en cero.
    Retorna un diccionario con los contadores y una lista vacía para el historial.
    """
    # DICCIONARIO: estructura clave-valor para organizar el estado del juego
    marcador = {
        "victorias": 0,
        "derrotas": 0,
        "empates": 0,
        # LISTA: almacena el historial de rondas. Empieza vacía y crece con .append()
        "historial": []
    }
    return marcador


def actualizar_marcador(marcador, jugada_usuario, jugada_cpu, resultado):
    """
    Actualiza el marcador según el resultado de la ronda.
    También registra los detalles de la ronda en el historial.
    resultado puede ser: "victoria", "derrota" o "empate"
    """
    if resultado == "victoria":
        marcador["victorias"] = marcador["victorias"] + 1
    elif resultado == "derrota":
        marcador["derrotas"] = marcador["derrotas"] + 1
    else:
        marcador["empates"] = marcador["empates"] + 1

    # DICCIONARIO dentro de LISTA: cada ronda se guarda como un diccionario
    # con los detalles de esa jugada, y se agrega al historial con .append()
    ronda = {
        "numero": len(marcador["historial"]) + 1,
        "jugada_usuario": jugada_usuario,
        "jugada_cpu": jugada_cpu,
        "resultado": resultado
    }
    marcador["historial"].append(ronda)

    return marcador