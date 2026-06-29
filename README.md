# piedra-papel-tijera
Juego Piedra, Papel o Tijera en Python - Proyecto académico
Juego Piedra, Papel o Tijera

Proyecto Integrador — Lógica de Programación

Facultad de Ingeniería en Sistemas y Computación


Nombre del proyecto

El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas

Sistema desarrollado: Juego Piedra, Papel o Tijera en Python 3


Integrantes

NombreCarreraSamuel CadenaIngeniería en ia 


Objetivo del sistema

Desarrollar un sistema interactivo de consola que permita a un usuario humano competir contra la computadora en el juego clásico de Piedra, Papel o Tijera, aplicando los conceptos de las cuatro unidades del curso: análisis y diseño de software, estructuras lógicas, organización del código y estructuras de datos con funciones.


Descripción de funcionalidades


Validación de entrada: el sistema verifica que el usuario escriba una opción válida (piedra, papel o tijera). Si la entrada es incorrecta, solicita una nueva jugada usando un bucle while.
Jugada de la CPU: la computadora genera su elección de forma pseudoaleatoria con distribución uniforme (P = 1/3 para cada opción), usando random.choice() sobre una tupla de opciones.
Evaluación del resultado: el sistema aplica la tabla de dominancia cíclica del juego mediante estructuras condicionales if / elif / else para determinar si el resultado de cada ronda es victoria, derrota o empate.
Marcador acumulado: se mantiene un diccionario con los contadores de victorias, derrotas y empates durante toda la partida.
Historial de rondas: cada ronda jugada se registra como un diccionario dentro de una lista, usando el método .append(). Al finalizar la partida, se muestra el historial completo iterando la lista con un bucle for.
Fin de partida: el juego termina automáticamente cuando el usuario o la computadora alcanza 2 victorias (mejor de 3 rondas configurables).



Estructura del repositorio

piedra-papel-tijera/
│
├── README.md
├── .gitignore
│
├── src/                        ← código fuente
│   ├── main.py                 punto de entrada
│   ├── game_engine.py          orquesta el flujo del juego
│   ├── rules.py                evalúa el ganador de cada ronda
│   ├── cpu_player.py           genera la jugada aleatoria de la CPU
│   ├── input_handler.py        captura y valida la entrada del usuario
│   ├── score_manager.py        marcador e historial de rondas
│   ├── display.py              muestra resultados e historial
│   ├── ui.py                   mensajes de bienvenida y despedida
│   └── constants.py            tupla de opciones y mensajes del sistema
│
└── docs/                       ← diagramas y documentación
    ├── Diagrama_Flujo_PiedraPapelTijera.docx
    └── Proyecto_Integrador_PiedraPapelTijera.docx


Conceptos de la Unidad 4 aplicados

ConceptoArchivoAplicaciónTuplaconstants.pyOPCIONES_VALIDAS = ("piedra", "papel", "tijera") — inmutable por diseñoListascore_manager.py"historial": [] crece con .append() en cada rondaDiccionarioscore_manager.pyMarcador y cada ronda guardados como pares clave-valorFuncióndisplay.pymostrar_historial() itera la lista con for y usa .get()


Cómo ejecutar el programa

Requisitos: Python 3.x instalado

bash# 1. Clonar el repositorio
git clone https://github.com/samu13cadena-gif/piedra-papel-tijera.git

# 2. Entrar a la carpeta del código
cd piedra-papel-tijera/src

# 3. Ejecutar el programa
python3 main.py


Fecha

28 Junio 2026
