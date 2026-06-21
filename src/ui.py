from constants import MENSAJE_BIENVENIDA, MENSAJE_DESPEDIDA


def mostrar_bienvenida():
    print(MENSAJE_BIENVENIDA)
    print("Juega al mejor de 3 rondas contra la computadora.\n")


def mostrar_menu():
    print("Elige tu jugada:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")


def mostrar_despedida(marcador):
    print("\n" + MENSAJE_DESPEDIDA)
    print(f"Resultado final -> Victorias: {marcador['victorias']}, "
          f"Derrotas: {marcador['derrotas']}, "
          f"Empates: {marcador['empates']}")