#!/usr/bin/env python3
"""
Regla del Trapecio Compuesta
Integración numérica

Fórmula: ∫[a,b] f(x)dx ≈ (h/2) [f(x0) + 2·Σf(xi) + f(xn)]
Error de truncamiento: O(h²)
"""

import math
import sys


# ─────────────────────────────────────────────
#  Colores ANSI
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
    MAGENTA= "\033[95m"


def titulo(texto):
    ancho = 64
    print()
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)
    print(C.CYAN + C.BOLD + texto.center(ancho) + C.RESET)
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)


def paso(n, texto):
    print(f"\n  {C.BLUE}{C.BOLD}[{n}]{C.RESET} {texto}")


def resultado(etiqueta, valor, color=C.GREEN):
    print(f"      {C.DIM}{etiqueta:<28}{C.RESET}{color}{C.BOLD}{valor}{C.RESET}")


def pedir_float(prompt, default=None):
    while True:
        try:
            entrada = input(prompt).strip()
            if entrada == "" and default is not None:
                return default
            return float(entrada)
        except ValueError:
            print(f"  {C.RED}Ingresa un número válido.{C.RESET}")


def pedir_int(prompt, default=None, minimo=1):
    while True:
        try:
            entrada = input(prompt).strip()
            if entrada == "" and default is not None:
                return default
            v = int(entrada)
            if v < minimo:
                print(f"  {C.RED}El valor mínimo es {minimo}.{C.RESET}")
            else:
                return v
        except ValueError:
            print(f"  {C.RED}Ingresa un entero válido.{C.RESET}")


# ─────────────────────────────────────────────
#  Núcleo del método
# ─────────────────────────────────────────────
def trapecio(f, a, b, n):
    """
    Regla del trapecio compuesta.

    Parámetros
    ----------
    f : callable — función a integrar
    a : float    — límite inferior
    b : float    — límite superior
    n : int      — número de subintervalos

    Retorna
    -------
    (integral, h, xs, ys)
    """
    h  = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    ys = [f(x) for x in xs]

    suma = ys[0] + ys[-1] + 2 * sum(ys[1:-1])
    integral = (h / 2) * suma

    return integral, h, xs, ys


def mostrar_pasos(f, a, b, n, integral_exacta=None, nombre_f="f(x)"):
    """Muestra el procedimiento completo paso a paso."""
    integral, h, xs, ys = trapecio(f, a, b, n)

    titulo("REGLA DEL TRAPECIO COMPUESTA")

    # ── Paso 1 ──
    paso(1, "Definición de parámetros iniciales")
    resultado("Límite inferior  a =", f"{a}")
    resultado("Límite superior  b =", f"{b}")
    resultado("Subintervalos    n =", f"{n}")
    resultado("Función            =", nombre_f)

    # ── Paso 2 ──
    paso(2, "Cálculo del tamaño del paso h")
    print(f"      {C.DIM}h = (b - a) / n = ({b} - {a}) / {n}{C.RESET}")
    resultado("h =", f"{h:.10g}")

    # ── Paso 3 & 4 ──
    paso(3, "Generación de nodos xᵢ = a + i·h y evaluación de f(xᵢ)")
    print()

    # Cabecera de tabla
    col_i  = 6
    col_x  = 18
    col_fx = 18
    col_w  = 10
    col_wfx= 18
    sep = "  "
    hdr = (f"  {'i':>{col_i}}{sep}{'xᵢ':>{col_x}}{sep}"
           f"{'f(xᵢ)':>{col_fx}}{sep}{'peso':>{col_w}}{sep}{'peso·f(xᵢ)':>{col_wfx}}")
    print(C.DIM + hdr + C.RESET)
    print("  " + "─" * (col_i + col_x + col_fx + col_w + col_wfx + 4 * len(sep)))

    suma_ponderada = 0.0
    for i, (x, y) in enumerate(zip(xs, ys)):
        peso = 1 if (i == 0 or i == n) else 2
        wy   = peso * y
        suma_ponderada += wy

        if i == 0 or i == n:
            color = C.MAGENTA
            tag   = " ← extremo"
        else:
            color = C.RESET
            tag   = ""

        fila = (f"  {i:>{col_i}}{sep}{x:>{col_x}.8f}{sep}"
                f"{y:>{col_fx}.8f}{sep}{peso:>{col_w}}{sep}{wy:>{col_wfx}.8f}{tag}")
        print(color + fila + C.RESET)

    # ── Paso 5 ──
    paso(4, "Cálculo de la suma ponderada")
    print(f"      {C.DIM}f(x₀) + 2·[f(x₁)+...+f(x_{{n-1}})] + f(xₙ){C.RESET}")
    resultado("Suma ponderada =", f"{suma_ponderada:.10g}")

    # ── Paso 6 ──
    paso(5, "Aplicación de la fórmula final")
    print(f"      {C.DIM}∫ f(x)dx ≈ (h/2) · suma = ({h:.6g}/2) · {suma_ponderada:.8g}{C.RESET}")
    resultado("Integral ≈", f"{integral:.10g}", color=C.GREEN)

    # ── Error ──
    paso(6, "Estimación del error")
    resultado("h²  (O(h²)) =", f"{h**2:.2e}")
    if integral_exacta is not None:
        exacta    = integral_exacta(a, b)
        error_abs = abs(integral - exacta)
        error_rel = abs(error_abs / exacta) * 100 if exacta != 0 else float("inf")
        resultado("Valor exacto      =", f"{exacta:.10g}", color=C.CYAN)
        resultado("Error absoluto    =", f"{error_abs:.2e}", color=C.YELLOW)
        resultado("Error relativo    =", f"{error_rel:.6f} %", color=C.YELLOW)

    print()
    print("─" * 64)
    print()
    return integral


# ─────────────────────────────────────────────
#  Análisis de convergencia
# ─────────────────────────────────────────────
def analisis_convergencia(f, a, b, integral_exacta=None, ns=None):
    """Muestra cómo mejora la aproximación al aumentar n."""
    if ns is None:
        ns = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    titulo("ANÁLISIS DE CONVERGENCIA")
    print()

    if integral_exacta is not None:
        exacta = integral_exacta(a, b)
        print(f"  {'n':>6}  {'h':>12}  {'Integral ≈':>16}  {'Error abs':>14}  {'Error rel (%)':>14}")
        print(f"  {'─'*6}  {'─'*12}  {'─'*16}  {'─'*14}  {'─'*14}")
        for n in ns:
            intg, h, _, _ = trapecio(f, a, b, n)
            ea = abs(intg - exacta)
            er = abs(ea / exacta) * 100 if exacta != 0 else float("inf")
            print(f"  {n:>6}  {h:>12.6f}  {intg:>16.8f}  {ea:>14.2e}  {er:>14.6f}")
    else:
        print(f"  {'n':>6}  {'h':>12}  {'Integral ≈':>16}")
        print(f"  {'─'*6}  {'─'*12}  {'─'*16}")
        for n in ns:
            intg, h, _, _ = trapecio(f, a, b, n)
            print(f"  {n:>6}  {h:>12.6f}  {intg:>16.8f}")

    print()


# ─────────────────────────────────────────────
#  Modo tabla de datos
# ─────────────────────────────────────────────
def trapecio_tabla(puntos):
    """
    Regla del trapecio sobre una tabla de puntos igualmente espaciados.

    Parámetros
    ----------
    puntos : list of (float, float) — pares (x, f(x))
    """
    puntos_ord = sorted(puntos, key=lambda p: p[0])
    xs = [p[0] for p in puntos_ord]
    ys = [p[1] for p in puntos_ord]
    n  = len(xs) - 1

    if n < 1:
        raise ValueError("Se necesitan al menos 2 puntos.")

    hs = [xs[i+1] - xs[i] for i in range(n)]
    h_prom = sum(hs) / len(hs)
    uniforme = all(abs(hi - h_prom) < 1e-9 for hi in hs)

    titulo("REGLA DEL TRAPECIO — TABLA DE DATOS")

    paso(1, "Tabla ingresada")
    print()
    col_i = 6; col_x = 16; col_fx = 16; col_w = 8; col_wfx = 16
    sep = "  "
    hdr = (f"  {'i':>{col_i}}{sep}{'xᵢ':>{col_x}}{sep}"
           f"{'f(xᵢ)':>{col_fx}}{sep}{'peso':>{col_w}}{sep}{'peso·f(xᵢ)':>{col_wfx}}")
    print(C.DIM + hdr + C.RESET)
    print("  " + "─"*(col_i+col_x+col_fx+col_w+col_wfx+4*len(sep)))

    if uniforme:
        suma_pond = ys[0] + ys[-1] + 2 * sum(ys[1:-1])
        integral  = (h_prom / 2) * suma_pond
        for i, (x, y) in enumerate(zip(xs, ys)):
            peso = 1 if (i == 0 or i == n) else 2
            color = C.MAGENTA if (i == 0 or i == n) else C.RESET
            tag   = " ← extremo" if (i == 0 or i == n) else ""
            fila = (f"  {i:>{col_i}}{sep}{x:>{col_x}.8f}{sep}"
                    f"{y:>{col_fx}.8f}{sep}{peso:>{col_w}}{sep}{peso*y:>{col_wfx}.8f}{tag}")
            print(color + fila + C.RESET)

        paso(2, "Parámetros deducidos de la tabla")
        resultado("a =", f"{xs[0]:.8g}")
        resultado("b =", f"{xs[-1]:.8g}")
        resultado("n =", f"{n}")
        resultado("h =", f"{h_prom:.8g}")

        paso(3, "Suma ponderada")
        resultado("Suma =", f"{suma_pond:.10g}")

        paso(4, "Integral aproximada")
        print(f"      {C.DIM}(h/2) · suma = ({h_prom:.6g}/2) · {suma_pond:.8g}{C.RESET}")
        resultado("Integral ≈", f"{integral:.10g}", color=C.GREEN)

    else:
        # Espaciado no uniforme: suma de trapecios individuales
        print(f"  {C.YELLOW}Advertencia: espaciado no uniforme. "
              f"Se aplicará la suma de trapecios individuales.{C.RESET}\n")
        integral = 0.0
        for i in range(n):
            trap_i = (xs[i+1] - xs[i]) / 2 * (ys[i] + ys[i+1])
            peso   = "—"
            fila   = (f"  {i:>{col_i}}{sep}{xs[i]:>{col_x}.8f}{sep}"
                      f"{ys[i]:>{col_fx}.8f}{sep}{peso:>{col_w}}{sep}{trap_i:>{col_wfx}.8f}")
            print(fila)
            integral += trap_i

        paso(2, "Suma de trapecios individuales")
        resultado("Integral ≈", f"{integral:.10g}", color=C.GREEN)

    print()
    print("─" * 64)
    print()
    return integral


# ─────────────────────────────────────────────
#  Catálogo de funciones de ejemplo
# ─────────────────────────────────────────────
FUNCIONES = [
    {
        "nombre": "sin(x)  en [0, π]",
        "f"     : math.sin,
        "a"     : 0.0,
        "b"     : math.pi,
        "exacta": lambda a, b: -math.cos(b) + math.cos(a),
        "desc"  : "∫₀^π sin(x)dx = 2",
    },
    {
        "nombre": "x²  en [0, 1]",
        "f"     : lambda x: x**2,
        "a"     : 0.0,
        "b"     : 1.0,
        "exacta": lambda a, b: (b**3 - a**3) / 3,
        "desc"  : "∫₀¹ x² dx = 1/3",
    },
    {
        "nombre": "exp(x)  en [0, 1]",
        "f"     : math.exp,
        "a"     : 0.0,
        "b"     : 1.0,
        "exacta": lambda a, b: math.exp(b) - math.exp(a),
        "desc"  : "∫₀¹ eˣ dx = e-1",
    },
    {
        "nombre": "1/x  en [1, 2]",
        "f"     : lambda x: 1/x,
        "a"     : 1.0,
        "b"     : 2.0,
        "exacta": lambda a, b: math.log(b) - math.log(a),
        "desc"  : "∫₁² (1/x) dx = ln(2)",
    },
    {
        "nombre": "sqrt(x)  en [0, 4]",
        "f"     : math.sqrt,
        "a"     : 0.0,
        "b"     : 4.0,
        "exacta": lambda a, b: (2/3)*(b**1.5 - a**1.5),
        "desc"  : "∫₀⁴ √x dx = 16/3",
    },
    {
        "nombre": "x·sin(x)  en [0, π]",
        "f"     : lambda x: x * math.sin(x),
        "a"     : 0.0,
        "b"     : math.pi,
        "exacta": lambda a, b: math.sin(b) - b*math.cos(b) - (math.sin(a) - a*math.cos(a)),
        "desc"  : "∫₀^π x·sin(x)dx = π",
    },
]


# ─────────────────────────────────────────────
#  Menús
# ─────────────────────────────────────────────
def menu_funcion():
    titulo("MODO: FUNCIÓN f(x)")
    print()
    print("  Selecciona una función de ejemplo o ingresa la tuya:\n")
    for i, fn in enumerate(FUNCIONES, 1):
        print(f"  {C.BLUE}[{i}]{C.RESET} {fn['nombre']:<22}  {C.DIM}{fn['desc']}{C.RESET}")
    print(f"  {C.BLUE}[{len(FUNCIONES)+1}]{C.RESET} Ingresar función personalizada")
    print()

    opcion = input("  Opción: ").strip()

    if opcion in [str(i) for i in range(1, len(FUNCIONES) + 2)]:
        idx = int(opcion) - 1
        if idx < len(FUNCIONES):
            fn      = FUNCIONES[idx]
            f       = fn["f"]
            nombre  = fn["nombre"]
            a_def   = fn["a"]
            b_def   = fn["b"]
            exacta  = fn["exacta"]
        else:
            expr   = input("\n  f(x) en Python (ej. math.sin(x)*x**2):\n  f(x) = ").strip()
            expr_e = input("  Integral exacta como función de a,b (Enter para omitir):\n  I(a,b) = ").strip()
            nombre = expr
            try:
                f = lambda x, e=expr: eval(e, {"x": x, "math": math, **vars(math)})
                f(1.0)
            except Exception as ex:
                print(f"  {C.RED}Error: {ex}{C.RESET}"); return
            a_def, b_def = 0.0, 1.0
            exacta = None
            if expr_e:
                try:
                    exacta = lambda a, b, e=expr_e: eval(e, {"a": a, "b": b, "math": math, **vars(math)})
                    exacta(0.0, 1.0)
                except Exception as ex:
                    print(f"  {C.YELLOW}No se pudo evaluar la exacta: {ex}{C.RESET}")
                    exacta = None
    else:
        print(f"  {C.RED}Opción inválida.{C.RESET}"); return

    print()
    a = pedir_float(f"  Límite inferior a [default={a_def}]: ", default=a_def)
    b = pedir_float(f"  Límite superior b [default={b_def}]: ", default=b_def)
    if a >= b:
        print(f"  {C.RED}Se requiere a < b.{C.RESET}"); return
    n = pedir_int("  Número de subintervalos n [default=4]: ", default=4, minimo=1)

    print()
    mostrar_pasos(f, a, b, n, integral_exacta=exacta, nombre_f=nombre)

    conv = input("  ¿Ver análisis de convergencia? [s/N]: ").strip().lower()
    if conv == "s":
        analisis_convergencia(f, a, b, integral_exacta=exacta)


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

    if len(puntos) < 2:
        print(f"  {C.RED}Se necesitan al menos 2 puntos.{C.RESET}"); return

    print()
    try:
        trapecio_tabla(puntos)
    except ValueError as e:
        print(f"  {C.RED}Error: {e}{C.RESET}\n")


def ejemplo_rapido():
    titulo("EJEMPLO RÁPIDO — sin(x) en [0, π], n=4")
    print()
    fn = FUNCIONES[0]
    mostrar_pasos(fn["f"], fn["a"], fn["b"], 4,
                  integral_exacta=fn["exacta"], nombre_f=fn["nombre"])
    analisis_convergencia(fn["f"], fn["a"], fn["b"], integral_exacta=fn["exacta"])


def main():
    print()
    print(C.CYAN + C.BOLD + "  ╔══════════════════════════════════════════════╗" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║       REGLA DEL TRAPECIO COMPUESTA          ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║         Métodos Numéricos — Python           ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ╚══════════════════════════════════════════════╝" + C.RESET)

    while True:
        print()
        print(f"  {C.BOLD}Menú principal{C.RESET}")
        print(f"  {C.BLUE}[1]{C.RESET} Resolver con función f(x)")
        print(f"  {C.BLUE}[2]{C.RESET} Resolver con tabla de datos")
        print(f"  {C.BLUE}[3]{C.RESET} Ejemplo rápido (sin(x) en [0,π], n=4)")
        print(f"  {C.BLUE}[0]{C.RESET} Salir")
        print()

        op = input("  Opción: ").strip()
        if op == "1":
            menu_funcion()
        elif op == "2":
            menu_tabla()
        elif op == "3":
            ejemplo_rapido()
        elif op == "0":
            print(f"\n  {C.DIM}Hasta luego.{C.RESET}\n")
            sys.exit(0)
        else:
            print(f"  {C.RED}Opción no válida.{C.RESET}")


if __name__ == "__main__":
    main()