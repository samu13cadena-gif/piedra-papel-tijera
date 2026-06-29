# display.py
# Este archivo muestra en pantalla el resultado de cada ronda y el marcador.

def mostrar_resultado_ronda(jugada_usuario, jugada_cpu, resultado, marcador):
    """
    Muestra las jugadas de ambos, el resultado de la ronda y el marcador actualizado.
    Usa el método .get() del diccionario para acceder a los valores de forma segura.
    """
    print(f"\nTú elegiste: {jugada_usuario}")
    print(f"La computadora eligió: {jugada_cpu}")

    if resultado == "victoria":
        print("¡Ganaste esta ronda!")
    elif resultado == "derrota":
        print("Perdiste esta ronda.")
    else:
        print("Empate en esta ronda.")

    # .get() es un método del diccionario que accede al valor de una clave
    print(f"Marcador -> Victorias: {marcador.get('victorias')}, "
          f"Derrotas: {marcador.get('derrotas')}, "
          f"Empates: {marcador.get('empates')}\n")


def mostrar_historial(historial):
    """
    Muestra el resumen de todas las rondas jugadas.
    Usa un bucle for para iterar la lista de diccionarios del historial.
    Esto aplica las estructuras: LISTA (historial) + FOR + DICCIONARIO (cada ronda).
    """
    print("\n--- RESUMEN DE LA PARTIDA ---")

    # BUCLE FOR sobre la LISTA de rondas: recorre cada diccionario del historial
    for ronda in historial:
        numero = ronda.get("numero")
        jugador = ronda.get("jugada_usuario")
        cpu = ronda.get("jugada_cpu")
        res = ronda.get("resultado")
        print(f"  Ronda {numero}: Tú={jugador} | CPU={cpu} | Resultado={res}")

    print("-----------------------------")