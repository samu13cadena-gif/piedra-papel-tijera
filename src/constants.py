# constants.py
# Este archivo guarda los valores fijos que usa todo el programa.

# TUPLA: se usa tupla porque las opciones del juego nunca cambian.
# Las tuplas son inmutables, lo que garantiza que nadie pueda
# modificar accidentalmente las opciones válidas del juego.
OPCIONES_VALIDAS = ("piedra", "papel", "tijera")

# Número de victorias necesarias para ganar la partida (mejor de 3)
VICTORIAS_PARA_GANAR = 2

# Mensajes del juego
MENSAJE_BIENVENIDA = "=== JUEGO PIEDRA, PAPEL O TIJERA ==="
MENSAJE_ENTRADA_INVALIDA = "Opción no válida. Escribe: piedra, papel o tijera."
MENSAJE_DESPEDIDA = "Gracias por jugar. ¡Hasta la próxima!"