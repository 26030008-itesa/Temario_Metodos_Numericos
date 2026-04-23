"""
Regla de Simpson 1/3 - Implementación compuesta
================================================
Integración numérica mediante parábolas de segundo grado.

Uso:
    python simpson_un_tercio.py

Dependencias: solo Python estándar (math). Sin librerías externas.
"""

import math


# ─────────────────────────────────────────────
#  Funciones disponibles para integrar
# ─────────────────────────────────────────────
FUNCIONES = {
    "1": {
        "nombre": "sin(x)",
        "f":      lambda x: math.sin(x),
        "exacta": lambda a, b: -math.cos(b) + math.cos(a),
    },
    "2": {
        "nombre": "cos(x)",
        "f":      lambda x: math.cos(x),
        "exacta": lambda a, b: math.sin(b) - math.sin(a),
    },
    "3": {
        "nombre": "x²",
        "f":      lambda x: x ** 2,
        "exacta": lambda a, b: (b**3 - a**3) / 3,
    },
    "4": {
        "nombre": "x³",
        "f":      lambda x: x ** 3,
        "exacta": lambda a, b: (b**4 - a**4) / 4,
    },
    "5": {
        "nombre": "eˣ",
        "f":      lambda x: math.exp(x),
        "exacta": lambda a, b: math.exp(b) - math.exp(a),
    },
    "6": {
        "nombre": "√x  (solo x ≥ 0)",
        "f":      lambda x: math.sqrt(max(0.0, x)),
        "exacta": lambda a, b: (2 / 3) * (max(0.0, b)**1.5 - max(0.0, a)**1.5),
    },
    "7": {
        "nombre": "x² + 2x + 1",
        "f":      lambda x: x**2 + 2*x + 1,
        "exacta": lambda a, b: (b**3/3 + b**2 + b) - (a**3/3 + a**2 + a),
    },
}


# ─────────────────────────────────────────────
#  Algoritmo de Simpson 1/3 compuesto
# ─────────────────────────────────────────────
def simpson_un_tercio(f, a, b, n):
    """
    Calcula la integral de f en [a, b] usando la regla compuesta de Simpson 1/3.

    Parámetros
    ----------
    f : callable  Función a integrar.
    a : float     Límite inferior.
    b : float     Límite superior.
    n : int       Número de subintervalos (debe ser par y >= 2).

    Retorna
    -------
    resultado : float  Valor aproximado de la integral.
    nodos     : list   Lista de tuplas (i, xi, f(xi), peso, contribución).
    h         : float  Tamaño del paso.
    """
    if n < 2 or n % 2 != 0:
        raise ValueError(f"n debe ser un entero par >= 2. Valor recibido: {n}")

    h = (b - a) / n
    nodos = []
    suma = 0.0

    for i in range(n + 1):
        xi = a + i * h
        fi = f(xi)

        if i == 0 or i == n:
            peso = 1
        elif i % 2 == 1:
            peso = 4
        else:
            peso = 2

        contribucion = peso * fi
        suma += contribucion
        nodos.append((i, xi, fi, peso, contribucion))

    resultado = (h / 3) * suma
    return resultado, nodos, h


# ─────────────────────────────────────────────
#  Utilidades de presentación
# ─────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
RED    = "\033[91m"
GRAY   = "\033[90m"
BLUE   = "\033[94m"

def color(texto, c):
    return f"{c}{texto}{RESET}"

def separador(ancho=65, char="─"):
    print(color(char * ancho, GRAY))

def encabezado(titulo):
    separador()
    print(color(f"  {titulo}", BOLD + CYAN))
    separador()

def imprimir_tabla(nodos):
    encabezado("Tabla de nodos")
    print(f"  {'i':>4}  {'xᵢ':>12}  {'f(xᵢ)':>14}  {'Peso':>5}  {'Contribución':>14}")
    separador()
    for (i, xi, fi, peso, contrib) in nodos:
        if i == 0 or i == len(nodos) - 1:
            peso_str = color(f"×{peso}", BLUE)
        elif peso == 4:
            peso_str = color(f"×{peso}", RED)
        else:
            peso_str = color(f"×{peso}", GREEN)

        print(f"  {i:>4}  {xi:>12.6f}  {fi:>14.8f}  {peso_str:>5}  {contrib:>14.8f}")
    separador()

def imprimir_resultados(resultado, exacto, h, n, nombre_fn):
    encabezado("Resultados")
    print(f"  Función integrada : {color(nombre_fn, YELLOW)}")
    print(f"  Subintervalos (n) : {n}")
    print(f"  Paso (h)          : {h:.8f}")
    separador()
    print(f"  {color('Resultado Simpson :', BOLD)}  {color(f'{resultado:.10f}', GREEN)}")
    if exacto is not None:
        error_abs = abs(resultado - exacto)
        error_rel = abs(error_abs / exacto) * 100 if exacto != 0 else float("inf")
        print(f"  {color('Valor exacto      :', BOLD)}  {color(f'{exacto:.10f}', CYAN)}")
        print(f"  Error absoluto    :  {error_abs:.2e}")
        print(f"  Error relativo    :  {error_rel:.6f} %")
    separador()


# ─────────────────────────────────────────────
#  Menú interactivo
# ─────────────────────────────────────────────
def pedir_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(color("  Entrada inválida. Ingresa un número.", RED))

def pedir_int_par(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 2:
                print(color("  n debe ser >= 2.", RED))
                continue
            if n % 2 != 0:
                print(color(f"  n debe ser par. Se ajusta a {n + 1}.", YELLOW))
                n += 1
            return n
        except ValueError:
            print(color("  Entrada inválida. Ingresa un entero.", RED))

def seleccionar_funcion():
    encabezado("Funciones disponibles")
    for k, v in FUNCIONES.items():
        print(f"  [{k}] {v['nombre']}")
    separador()
    while True:
        opcion = input("  Elige una función [1-7]: ").strip()
        if opcion in FUNCIONES:
            return FUNCIONES[opcion]
        print(color("  Opción inválida.", RED))

def menu_principal():
    print()
    print(color("  ╔══════════════════════════════════════════╗", CYAN))
    print(color("  ║     Regla de Simpson 1/3 Compuesta       ║", CYAN + BOLD))
    print(color("  ╚══════════════════════════════════════════╝", CYAN))
    print()

    while True:
        fn_data = seleccionar_funcion()
        print()
        a = pedir_float("  Límite inferior a = ")
        b = pedir_float("  Límite superior b = ")
        if a >= b:
            print(color("  Error: a debe ser menor que b.", RED))
            continue
        n = pedir_int_par("  Número de subintervalos n (par) = ")

        print()
        try:
            resultado, nodos, h = simpson_un_tercio(fn_data["f"], a, b, n)
        except ValueError as e:
            print(color(f"  Error: {e}", RED))
            continue

        exacto = None
        try:
            exacto = fn_data["exacta"](a, b)
        except Exception:
            pass

        imprimir_tabla(nodos)
        print()
        imprimir_resultados(resultado, exacto, h, n, fn_data["nombre"])

        print()
        otra = input("  ¿Calcular otra integral? [s/n]: ").strip().lower()
        if otra != "s":
            print()
            print(color("  ¡Hasta luego!", CYAN))
            print()
            break
        print()


# ─────────────────────────────────────────────
#  Punto de entrada
# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()