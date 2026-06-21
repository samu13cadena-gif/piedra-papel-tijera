def crear_marcador():
    marcador = {
        "victorias": 0,
        "derrotas": 0,
        "empates": 0
    }
    return marcador


def actualizar_marcador(marcador, resultado):
    if resultado == "victoria":
        marcador["victorias"] = marcador["victorias"] + 1
    elif resultado == "derrota":
        marcador["derrotas"] = marcador["derrotas"] + 1
    else:
        marcador["empates"] = marcador["empates"] + 1

    return marcador