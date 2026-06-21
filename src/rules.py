# rules.py
# Este archivo contiene las reglas del juego y decide quién gana cada ronda.

def determinar_resultado(jugada_usuario, jugada_cpu):
    """
    Compara la jugada del usuario contra la jugada de la CPU.
    Retorna "victoria", "derrota" o "empate" desde el punto de vista del usuario.

    Reglas:
    - Piedra vence a Tijera
    - Tijera vence a Papel
    - Papel vence a Piedra
    """

    # Caso 1: empate, ambos jugaron lo mismo
    if jugada_usuario == jugada_cpu:
        return "empate"

    # Caso 2: el usuario gana
    if jugada_usuario == "piedra" and jugada_cpu == "tijera":
        return "victoria"
    elif jugada_usuario == "tijera" and jugada_cpu == "papel":
        return "victoria"
    elif jugada_usuario == "papel" and jugada_cpu == "piedra":
        return "victoria"

    # Caso 3: si no fue empate ni victoria, entonces el usuario pierde
    else:
        return "derrota"