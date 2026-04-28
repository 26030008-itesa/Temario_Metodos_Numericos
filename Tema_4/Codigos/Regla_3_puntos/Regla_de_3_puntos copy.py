#!/usr/bin/env python3
"""
Método de 3 Puntos - Diferencia Central
Aproximación numérica de la derivada primera

Fórmula: f'(x0) ≈ [f(x0 + h) - f(x0 - h)] / (2h)
Error de truncamiento: O(h²)
"""

import math
import sys


# ─────────────────────────────────────────────
#  Colores ANSI para la terminal
# ─────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BLUE   = "\033[94m"
    DIM    = "\033[2m"


def titulo(texto):
    ancho = 60
    print()
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)
    print(C.CYAN + C.BOLD + texto.center(ancho) + C.RESET)
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)


def paso(n, texto):
    print(f"  {C.BLUE}{C.BOLD}[{n}]{C.RESET} {texto}")


def resultado(etiqueta, valor, color=C.GREEN):
    print(f"      {C.DIM}{etiqueta:<25}{C.RESET}{color}{C.BOLD}{valor}{C.RESET}")


# ─────────────────────────────────────────────
#  Núcleo del método
# ─────────────────────────────────────────────
def tres_puntos(f, x0, h):
    """
    Aplica la regla de diferencia central de 3 puntos.

    Parámetros
    ----------
    f  : callable  — función a derivar
    x0 : float     — punto donde se evalúa la derivada
    h  : float     — tamaño del paso

    Retorna
    -------
    (derivada, f_menos, f_mas)
    """
    f_menos = f(x0 - h)
    f_mas   = f(x0 + h)
    derivada = (f_mas - f_menos) / (2 * h)
    return derivada, f_menos, f_mas


def mostrar_pasos(f, x0, h, derivada_exacta=None):
    """Muestra el procedimiento completo paso a paso."""
    derivada, f_menos, f_mas = tres_puntos(f, x0, h)

    titulo("MÉTODO DE 3 PUNTOS — DIFERENCIA CENTRAL")

    print()
    paso(1, f"Definir el punto y el paso")
    resultado("x₀ =", f"{x0}")
    resultado("h  =", f"{h}")

    print()
    paso(2, "Identificar los nodos")
    resultado("x₀ - h =", f"{x0 - h:.10g}")
    resultado("x₀ + h =", f"{x0 + h:.10g}")

    print()
    paso(3, "Evaluar la función en los nodos")
    resultado("f(x₀ - h) =", f"{f_menos:.10g}")
    resultado("f(x₀ + h) =", f"{f_mas:.10g}")

    print()
    paso(4, "Aplicar la fórmula")
    print(f"      {C.DIM}f'(x₀) ≈ [f(x₀+h) - f(x₀-h)] / 2h{C.RESET}")
    print(f"      {C.DIM}       = [{f_mas:.10g} - ({f_menos:.10g})] / (2 × {h}){C.RESET}")
    resultado("f'(x₀) ≈", f"{derivada:.10g}", color=C.GREEN)

    print()
    paso(5, "Estimar el error (O(h²))")
    resultado("h²  =", f"{h**2:.2e}")

    if derivada_exacta is not None:
        exacta = derivada_exacta(x0)
        error_abs = abs(derivada - exacta)
        error_rel = abs(error_abs / exacta) * 100 if exacta != 0 else float("inf")
        resultado("Valor exacto  =", f"{exacta:.10g}", color=C.CYAN)
        resultado("Error absoluto =", f"{error_abs:.2e}", color=C.YELLOW)
        resultado("Error relativo =", f"{error_rel:.4f} %", color=C.YELLOW)

    print()
    print("─" * 60)
    print()
    return derivada


# ─────────────────────────────────────────────
#  Modo tabla de datos
# ─────────────────────────────────────────────
def tres_puntos_tabla(puntos, x0):
    """
    Aplica diferencia central sobre una tabla de puntos (x, f(x)).

    Parámetros
    ----------
    puntos : list of (float, float)
    x0     : float — debe coincidir con algún x de la tabla

    Retorna
    -------
    derivada aproximada
    """
    puntos_ord = sorted(puntos, key=lambda p: p[0])
    xs = [p[0] for p in puntos_ord]
    ys = [p[1] for p in puntos_ord]

    try:
        idx = next(i for i, x in enumerate(xs) if abs(x - x0) < 1e-12)
    except StopIteration:
        raise ValueError(f"x₀ = {x0} no se encontró en la tabla.")

    if idx == 0:
        raise ValueError("x₀ es el primer punto; no hay nodo izquierdo.")
    if idx == len(xs) - 1:
        raise ValueError("x₀ es el último punto; no hay nodo derecho.")

    xm, fm = xs[idx - 1], ys[idx - 1]
    xp, fp = xs[idx + 1], ys[idx + 1]
    h1 = x0 - xm
    h2 = xp - x0

    if abs(h1 - h2) > 1e-8:
        print(f"  {C.YELLOW}Advertencia: h₁ ({h1:.4g}) ≠ h₂ ({h2:.4g}). "
              f"Se usará diferencia central generalizada.{C.RESET}")

    derivada = (fp - fm) / (xp - xm)

    titulo("MÉTODO DE 3 PUNTOS — TABLA DE DATOS")
    print()
    paso(1, "Tabla ordenada ingresada")
    print(f"      {'x':>12}  {'f(x)':>14}")
    print(f"      {'─'*12}  {'─'*14}")
    for i, (x, y) in enumerate(puntos_ord):
        marca = " ◄" if abs(x - x0) < 1e-12 else (
                " ←" if i == idx - 1 else (
                " →" if i == idx + 1 else ""))
        color = C.GREEN if marca else C.RESET
        print(f"      {color}{x:>12.6g}  {y:>14.6g}{marca}{C.RESET}")

    print()
    paso(2, "Nodos identificados")
    resultado("x₀ - h =", f"{xm:.10g}")
    resultado("f(x₀-h) =", f"{fm:.10g}")
    resultado("x₀ + h =", f"{xp:.10g}")
    resultado("f(x₀+h) =", f"{fp:.10g}")

    print()
    paso(3, "Aplicar la fórmula")
    print(f"      {C.DIM}f'(x₀) ≈ [f(x₀+h) - f(x₀-h)] / (x₊ - x₋){C.RESET}")
    print(f"      {C.DIM}       = [{fp:.10g} - ({fm:.10g})] / {xp - xm:.4g}{C.RESET}")
    resultado("f'(x₀) ≈", f"{derivada:.10g}", color=C.GREEN)

    print()
    print("─" * 60)
    print()
    return derivada


# ─────────────────────────────────────────────
#  Análisis de convergencia
# ─────────────────────────────────────────────
def analisis_convergencia(f, x0, derivada_exacta=None, pasos=None):
    """Muestra cómo varía el resultado para distintos valores de h."""
    if pasos is None:
        pasos = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

    titulo("ANÁLISIS DE CONVERGENCIA")
    print()

    if derivada_exacta is not None:
        exacta = derivada_exacta(x0)
        print(f"  {'h':>10}  {'f\'(x₀)':>16}  {'Error abs':>14}  {'Error rel (%)':>14}")
        print(f"  {'─'*10}  {'─'*16}  {'─'*14}  {'─'*14}")
        for h in pasos:
            d, _, _ = tres_puntos(f, x0, h)
            ea = abs(d - exacta)
            er = abs(ea / exacta) * 100 if exacta != 0 else float("inf")
            print(f"  {h:>10.1e}  {d:>16.8f}  {ea:>14.2e}  {er:>14.4f}")
    else:
        print(f"  {'h':>10}  {'f\'(x₀)':>16}")
        print(f"  {'─'*10}  {'─'*16}")
        for h in pasos:
            d, _, _ = tres_puntos(f, x0, h)
            print(f"  {h:>10.1e}  {d:>16.8f}")

    print()


# ─────────────────────────────────────────────
#  Menú interactivo
# ─────────────────────────────────────────────
FUNCIONES_EJEMPLO = [
    ("sin(x)",     math.sin,  math.cos,  "Seno — derivada exacta: cos(x)"),
    ("cos(x)",     math.cos,  lambda x: -math.sin(x), "Coseno — derivada exacta: -sin(x)"),
    ("exp(x)",     math.exp,  math.exp,  "Exponencial — derivada exacta: exp(x)"),
    ("x³",         lambda x: x**3, lambda x: 3*x**2, "Cúbica — derivada exacta: 3x²"),
    ("ln(x)",      math.log,  lambda x: 1/x, "Logaritmo natural — derivada exacta: 1/x"),
    ("x²·sin(x)",  lambda x: x**2 * math.sin(x),
                   lambda x: 2*x*math.sin(x) + x**2*math.cos(x),
                   "x²·sin(x) — derivada exacta: 2x·sin(x)+x²·cos(x)"),
]


def pedir_float(prompt, default=None):
    while True:
        try:
            entrada = input(prompt).strip()
            if entrada == "" and default is not None:
                return default
            return float(entrada)
        except ValueError:
            print(f"  {C.RED}Ingresa un número válido.{C.RESET}")


def menu_funcion():
    titulo("MODO: FUNCIÓN f(x)")
    print()
    print("  Selecciona una función de ejemplo o ingresa la tuya:\n")
    for i, (_, _, _, desc) in enumerate(FUNCIONES_EJEMPLO, 1):
        print(f"  {C.BLUE}[{i}]{C.RESET} {desc}")
    print(f"  {C.BLUE}[7]{C.RESET} Ingresar función personalizada")
    print()

    opcion = input("  Opción: ").strip()

    if opcion in [str(i) for i in range(1, 8)]:
        idx = int(opcion) - 1
        if idx < 6:
            nombre, f, df, _ = FUNCIONES_EJEMPLO[idx]
            print(f"\n  {C.DIM}Función seleccionada: {nombre}{C.RESET}")
        else:
            expr = input("\n  Escribe f(x) en Python (usa math.sin, math.exp, etc.):\n  f(x) = ").strip()
            expr_d = input("  Escribe f'(x) exacta (Enter para omitir):\n  f'(x) = ").strip()
            try:
                f = lambda x, e=expr: eval(e, {"x": x, "math": math, **vars(math)})
                f(1.0)  # prueba rápida
            except Exception as ex:
                print(f"  {C.RED}Error en f(x): {ex}{C.RESET}")
                return
            df = None
            if expr_d:
                try:
                    df = lambda x, e=expr_d: eval(e, {"x": x, "math": math, **vars(math)})
                    df(1.0)
                except Exception as ex:
                    print(f"  {C.YELLOW}No se pudo evaluar f'(x): {ex}. Se omitirá el error.{C.RESET}")
                    df = None
    else:
        print(f"  {C.RED}Opción inválida.{C.RESET}")
        return

    print()
    x0 = pedir_float("  x₀ (punto de evaluación) [default=1.0]: ", default=1.0)
    h  = pedir_float("  h  (tamaño del paso)      [default=0.1]: ", default=0.1)

    print()
    mostrar_pasos(f, x0, h, derivada_exacta=df)

    conv = input("  ¿Ver análisis de convergencia? [s/N]: ").strip().lower()
    if conv == "s":
        analisis_convergencia(f, x0, derivada_exacta=df)


def menu_tabla():
    titulo("MODO: TABLA DE DATOS")
    print()
    print("  Ingresa los puntos como: x, f(x)  (uno por línea)")
    print("  Escribe 'fin' cuando termines.\n")

    puntos = []
    while True:
        linea = input(f"  Punto {len(puntos)+1}: ").strip()
        if linea.lower() == "fin":
            break
        try:
            partes = linea.replace(";", ",").split(",")
            x = float(partes[0])
            y = float(partes[1])
            puntos.append((x, y))
        except Exception:
            print(f"  {C.RED}Formato inválido. Usa: x, f(x){C.RESET}")

    if len(puntos) < 3:
        print(f"  {C.RED}Se necesitan al menos 3 puntos.{C.RESET}")
        return

    print()
    x0 = pedir_float("  x₀ (debe estar en la tabla): ")
    print()

    try:
        tres_puntos_tabla(puntos, x0)
    except ValueError as e:
        print(f"  {C.RED}Error: {e}{C.RESET}\n")


def menu_ejemplo_rapido():
    """Demuestra el método con sin(x) en x0=1, h=0.1 sin preguntar nada."""
    titulo("EJEMPLO RÁPIDO — sin(x) en x₀=1, h=0.1")
    print()
    mostrar_pasos(math.sin, x0=1.0, h=0.1, derivada_exacta=math.cos)
    analisis_convergencia(math.sin, x0=1.0, derivada_exacta=math.cos)


def main():
    print()
    print(C.CYAN + C.BOLD + "  ╔══════════════════════════════════════════════╗" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║   MÉTODO DE 3 PUNTOS — DIFERENCIA CENTRAL   ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║         Métodos Numéricos — Python           ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ╚══════════════════════════════════════════════╝" + C.RESET)

    while True:
        print()
        print(f"  {C.BOLD}Menú principal{C.RESET}")
        print(f"  {C.BLUE}[1]{C.RESET} Resolver con función f(x)")
        print(f"  {C.BLUE}[2]{C.RESET} Resolver con tabla de datos")
        print(f"  {C.BLUE}[3]{C.RESET} Ejemplo rápido (sin demostración)")
        print(f"  {C.BLUE}[0]{C.RESET} Salir")
        print()

        opcion = input("  Opción: ").strip()

        if opcion == "1":
            menu_funcion()
        elif opcion == "2":
            menu_tabla()
        elif opcion == "3":
            menu_ejemplo_rapido()
        elif opcion == "0":
            print(f"\n  {C.DIM}Hasta luego.{C.RESET}\n")
            sys.exit(0)
        else:
            print(f"  {C.RED}Opción no válida.{C.RESET}")


if __name__ == "__main__":
    main()