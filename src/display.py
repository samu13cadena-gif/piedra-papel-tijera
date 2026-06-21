def mostrar_resultado_ronda(jugada_usuario, jugada_cpu, resultado, marcador):
    print(f"\nTú elegiste: {jugada_usuario}")
    print(f"La computadora eligió: {jugada_cpu}")

    if resultado == "victoria":
        print("¡Ganaste esta ronda!")
    elif resultado == "derrota":
        print("Perdiste esta ronda.")
    else:
        print("Empate en esta ronda.")

    print(f"Marcador -> Victorias: {marcador['victorias']}, "
          f"Derrotas: {marcador['derrotas']}, "
          f"Empates: {marcador['empates']}\n")