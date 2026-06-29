# ui.py
# Este archivo muestra el menú y los mensajes al usuario.

from constants import MENSAJE_BIENVENIDA, MENSAJE_DESPEDIDA


def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida al iniciar el juego.
    """
    print(MENSAJE_BIENVENIDA)
    print("Juega al mejor de 3 rondas contra la computadora.\n")


def mostrar_menu():
    """
    Muestra las opciones disponibles para el usuario.
    """
    print("Elige tu jugada:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")


def mostrar_despedida(marcador):
    """
    Muestra el mensaje final con el marcador completo.
    Usa el método .items() del diccionario para iterar las claves y valores,
    excluyendo el historial (que es una lista, no un contador).
    """
    print("\n" + MENSAJE_DESPEDIDA)

    # .items() devuelve pares (clave, valor) del diccionario
    for clave, valor in marcador.items():
        # Saltamos el historial porque no es un contador numérico
        if clave != "historial":
            print(f"  {clave.capitalize()}: {valor}")