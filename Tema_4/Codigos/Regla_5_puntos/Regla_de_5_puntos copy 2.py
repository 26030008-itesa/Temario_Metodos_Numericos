#!/usr/bin/env python3
"""
Regla de 5 Puntos — Derivación Numérica
Aproximación de la primera derivada f'(x₀)

Fórmula de punto central:
  f'(x₀) ≈ (1/12h) [-f(x₀+2h) + 8f(x₀+h) - 8f(x₀-h) + f(x₀-2h)]
  Error: O(h⁴)

Fórmula de punto extremo (izquierdo):
  f'(x₀) ≈ (1/12h) [-25f(x₀) + 48f(x₀+h) - 36f(x₀+2h) + 16f(x₀+3h) - 3f(x₀+4h)]
  Error: O(h⁴)
"""

import math
import sys


# ─────────────────────────────────────────────
#  Colores ANSI
# ─────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BLUE    = "\033[94m"
    DIM     = "\033[2m"
    MAGENTA = "\033[95m"
    WHITE   = "\033[97m"


def titulo(texto):
    ancho = 66
    print()
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)
    print(C.CYAN + C.BOLD + texto.center(ancho) + C.RESET)
    print(C.CYAN + C.BOLD + "─" * ancho + C.RESET)


def subtitulo(texto):
    ancho = 66
    print()
    print(C.MAGENTA + C.BOLD + "  ┌─ " + texto + C.RESET)


def paso(n, texto):
    print(f"\n  {C.BLUE}{C.BOLD}[{n}]{C.RESET} {texto}")


def resultado(etiqueta, valor, color=C.GREEN):
    print(f"      {C.DIM}{etiqueta:<30}{C.RESET}{color}{C.BOLD}{valor}{C.RESET}")


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
#  Núcleos del método
# ─────────────────────────────────────────────
def cinco_puntos_central(f, x0, h):
    """
    Fórmula de 5 puntos — Punto central.

    f'(x₀) ≈ (1/12h)[-f(x₀+2h) + 8f(x₀+h) - 8f(x₀-h) + f(x₀-2h)]
    Error: O(h⁴)

    Nodos usados: x₀-2h, x₀-h, x₀, x₀+h, x₀+2h
    Coeficientes:    1,    -8,  0,    8,    -1   (dividido entre 12h)
    """
    xm2 = x0 - 2*h;  fm2 = f(xm2)
    xm1 = x0 - h;    fm1 = f(xm1)
    xp1 = x0 + h;    fp1 = f(xp1)
    xp2 = x0 + 2*h;  fp2 = f(xp2)

    derivada = (1 / (12 * h)) * (fm2 - 8*fm1 + 8*fp1 - fp2)

    nodos = [
        (xm2, fm2, 1,  "x₀ - 2h"),
        (xm1, fm1, -8, "x₀ - h "),
        (x0,  None, 0, "x₀     "),
        (xp1, fp1,  8, "x₀ + h "),
        (xp2, fp2, -1, "x₀ + 2h"),
    ]
    return derivada, nodos


def cinco_puntos_extremo(f, x0, h):
    """
    Fórmula de 5 puntos — Punto extremo (izquierdo / inicio).

    f'(x₀) ≈ (1/12h)[-25f(x₀) + 48f(x₀+h) - 36f(x₀+2h) + 16f(x₀+3h) - 3f(x₀+4h)]
    Error: O(h⁴)

    Nodos usados: x₀, x₀+h, x₀+2h, x₀+3h, x₀+4h
    Coeficientes: -25,   48,    -36,     16,    -3   (dividido entre 12h)
    """
    x0v  = x0;       f0  = f(x0v)
    xp1  = x0 + h;   fp1 = f(xp1)
    xp2  = x0 + 2*h; fp2 = f(xp2)
    xp3  = x0 + 3*h; fp3 = f(xp3)
    xp4  = x0 + 4*h; fp4 = f(xp4)

    derivada = (1 / (12 * h)) * (-25*f0 + 48*fp1 - 36*fp2 + 16*fp3 - 3*fp4)

    nodos = [
        (x0v, f0,  -25, "x₀      "),
        (xp1, fp1,  48, "x₀ + h  "),
        (xp2, fp2, -36, "x₀ + 2h "),
        (xp3, fp3,  16, "x₀ + 3h "),
        (xp4, fp4,  -3, "x₀ + 4h "),
    ]
    return derivada, nodos


# ─────────────────────────────────────────────
#  Mostrar pasos detallados
# ─────────────────────────────────────────────
def mostrar_pasos_central(f, x0, h, df_exacta=None):
    derivada, nodos = cinco_puntos_central(f, x0, h)

    subtitulo("FÓRMULA DE PUNTO CENTRAL")
    print(f"  {C.DIM}  f'(x₀) ≈ (1/12h)[-f(x₀+2h) + 8·f(x₀+h) - 8·f(x₀-h) + f(x₀-2h)]{C.RESET}")
    print(f"  {C.DIM}  Error de truncamiento: O(h⁴){C.RESET}")

    paso(1, "Definir el punto y el paso")
    resultado("x₀ =", f"{x0}")
    resultado("h  =", f"{h}")

    paso(2, "Identificar los 5 nodos")
    col_tag = 12; col_x = 18; col_c = 8
    print(f"\n      {C.DIM}{'Nodo':<{col_tag}}  {'xᵢ':>{col_x}}  {'coef':>{col_c}}{C.RESET}")
    print(f"      {'─'*(col_tag+col_x+col_c+4)}")
    for xv, fv, coef, tag in nodos:
        marca = C.MAGENTA if coef != 0 else C.DIM
        print(f"      {marca}{tag:<{col_tag}}  {xv:>{col_x}.8f}  {coef:>{col_c}}{C.RESET}")

    paso(3, "Evaluar f(x) en los nodos activos")
    col_x2 = 18; col_fv = 18; col_c2 = 8; col_cfv = 18
    print(f"\n      {C.DIM}{'xᵢ':>{col_x2}}  {'f(xᵢ)':>{col_fv}}  {'coef':>{col_c2}}  {'coef·f(xᵢ)':>{col_cfv}}{C.RESET}")
    print(f"      {'─'*(col_x2+col_fv+col_c2+col_cfv+6)}")
    suma = 0.0
    for xv, fv, coef, tag in nodos:
        if coef == 0:
            continue
        cfv = coef * fv
        suma += cfv
        print(f"      {xv:>{col_x2}.8f}  {fv:>{col_fv}.8f}  {coef:>{col_c2}}  {cfv:>{col_cfv}.8f}")
    print(f"      {'─'*(col_x2+col_fv+col_c2+col_cfv+6)}")
    print(f"      {'Suma ponderada':>{col_x2+col_fv+col_c2+3}}  {suma:>{col_cfv}.8f}")

    paso(4, "Aplicar la fórmula")
    print(f"      {C.DIM}f'(x₀) = (1 / 12·{h}) · {suma:.8f}{C.RESET}")
    resultado("f'(x₀) ≈", f"{derivada:.10g}", color=C.GREEN)

    paso(5, "Error de truncamiento")
    resultado("Orden del error  =", "O(h⁴)")
    resultado("h⁴ ≈", f"{h**4:.2e}")
    if df_exacta is not None:
        exacta    = df_exacta(x0)
        error_abs = abs(derivada - exacta)
        error_rel = abs(error_abs / exacta) * 100 if exacta != 0 else float("inf")
        resultado("Valor exacto     =", f"{exacta:.10g}", color=C.CYAN)
        resultado("Error absoluto   =", f"{error_abs:.2e}", color=C.YELLOW)
        resultado("Error relativo   =", f"{error_rel:.6f} %", color=C.YELLOW)

    return derivada


def mostrar_pasos_extremo(f, x0, h, df_exacta=None):
    derivada, nodos = cinco_puntos_extremo(f, x0, h)

    subtitulo("FÓRMULA DE PUNTO EXTREMO (inicio)")
    print(f"  {C.DIM}  f'(x₀) ≈ (1/12h)[-25·f(x₀) + 48·f(x₀+h) - 36·f(x₀+2h) + 16·f(x₀+3h) - 3·f(x₀+4h)]{C.RESET}")
    print(f"  {C.DIM}  Error de truncamiento: O(h⁴){C.RESET}")

    paso(1, "Definir el punto y el paso")
    resultado("x₀ =", f"{x0}")
    resultado("h  =", f"{h}")

    paso(2, "Identificar los 5 nodos (todos hacia la derecha)")
    col_tag = 12; col_x = 18; col_c = 8
    print(f"\n      {C.DIM}{'Nodo':<{col_tag}}  {'xᵢ':>{col_x}}  {'coef':>{col_c}}{C.RESET}")
    print(f"      {'─'*(col_tag+col_x+col_c+4)}")
    for xv, fv, coef, tag in nodos:
        print(f"      {C.MAGENTA}{tag:<{col_tag}}  {xv:>{col_x}.8f}  {coef:>{col_c}}{C.RESET}")

    paso(3, "Evaluar f(x) en los 5 nodos")
    col_x2 = 18; col_fv = 18; col_c2 = 8; col_cfv = 18
    print(f"\n      {C.DIM}{'xᵢ':>{col_x2}}  {'f(xᵢ)':>{col_fv}}  {'coef':>{col_c2}}  {'coef·f(xᵢ)':>{col_cfv}}{C.RESET}")
    print(f"      {'─'*(col_x2+col_fv+col_c2+col_cfv+6)}")
    suma = 0.0
    for xv, fv, coef, tag in nodos:
        cfv = coef * fv
        suma += cfv
        print(f"      {xv:>{col_x2}.8f}  {fv:>{col_fv}.8f}  {coef:>{col_c2}}  {cfv:>{col_cfv}.8f}")
    print(f"      {'─'*(col_x2+col_fv+col_c2+col_cfv+6)}")
    print(f"      {'Suma ponderada':>{col_x2+col_fv+col_c2+3}}  {suma:>{col_cfv}.8f}")

    paso(4, "Aplicar la fórmula")
    print(f"      {C.DIM}f'(x₀) = (1 / 12·{h}) · {suma:.8f}{C.RESET}")
    resultado("f'(x₀) ≈", f"{derivada:.10g}", color=C.GREEN)

    paso(5, "Error de truncamiento")
    resultado("Orden del error  =", "O(h⁴)")
    resultado("h⁴ ≈", f"{h**4:.2e}")
    if df_exacta is not None:
        exacta    = df_exacta(x0)
        error_abs = abs(derivada - exacta)
        error_rel = abs(error_abs / exacta) * 100 if exacta != 0 else float("inf")
        resultado("Valor exacto     =", f"{exacta:.10g}", color=C.CYAN)
        resultado("Error absoluto   =", f"{error_abs:.2e}", color=C.YELLOW)
        resultado("Error relativo   =", f"{error_rel:.6f} %", color=C.YELLOW)

    return derivada


# ─────────────────────────────────────────────
#  Comparación central vs extremo vs 3 puntos
# ─────────────────────────────────────────────
def comparacion(f, x0, h, df_exacta=None):
    titulo("COMPARACIÓN: 3 PUNTOS vs 5 PUNTOS CENTRAL vs 5 PUNTOS EXTREMO")
    print()

    # 3 puntos (diferencia central)
    d3 = (f(x0 + h) - f(x0 - h)) / (2 * h)
    # 5 puntos central
    d5c, _ = cinco_puntos_central(f, x0, h)
    # 5 puntos extremo
    d5e, _ = cinco_puntos_extremo(f, x0, h)

    col_m = 28; col_v = 18; col_e = 16; col_o = 10
    print(f"  {C.DIM}{'Método':<{col_m}}  {'f\'(x₀)':>{col_v}}  {'Error abs':>{col_e}}  {'Orden':>{col_o}}{C.RESET}")
    print(f"  {'─'*(col_m+col_v+col_e+col_o+6)}")

    metodos = [
        ("3 puntos (central)",       d3,  "O(h²)"),
        ("5 puntos (punto central)", d5c, "O(h⁴)"),
        ("5 puntos (punto extremo)", d5e, "O(h⁴)"),
    ]

    for nombre, d, orden in metodos:
        if df_exacta is not None:
            exacta = df_exacta(x0)
            ea = abs(d - exacta)
            ea_str = f"{ea:.2e}"
        else:
            ea_str = "—"
        print(f"  {nombre:<{col_m}}  {d:>{col_v}.8f}  {ea_str:>{col_e}}  {orden:>{col_o}}")

    if df_exacta is not None:
        exacta = df_exacta(x0)
        print(f"\n  {C.DIM}{'Valor exacto':<{col_m}}  {exacta:>{col_v}.8f}{C.RESET}")

    print()


# ─────────────────────────────────────────────
#  Análisis de convergencia
# ─────────────────────────────────────────────
def analisis_convergencia(f, x0, df_exacta=None, hs=None):
    if hs is None:
        hs = [1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-4, 1e-5]

    titulo("ANÁLISIS DE CONVERGENCIA  (ambas fórmulas)")
    print()

    if df_exacta is not None:
        exacta = df_exacta(x0)
        print(f"  {'h':>10}  {'5P-central':>16}  {'Error-C':>12}  {'5P-extremo':>16}  {'Error-E':>12}")
        print(f"  {'─'*10}  {'─'*16}  {'─'*12}  {'─'*16}  {'─'*12}")
        for h in hs:
            dc, _ = cinco_puntos_central(f, x0, h)
            de, _ = cinco_puntos_extremo(f, x0, h)
            ec = abs(dc - exacta)
            ee = abs(de - exacta)
            print(f"  {h:>10.1e}  {dc:>16.8f}  {ec:>12.2e}  {de:>16.8f}  {ee:>12.2e}")
    else:
        print(f"  {'h':>10}  {'5P-central':>16}  {'5P-extremo':>16}")
        print(f"  {'─'*10}  {'─'*16}  {'─'*16}")
        for h in hs:
            dc, _ = cinco_puntos_central(f, x0, h)
            de, _ = cinco_puntos_extremo(f, x0, h)
            print(f"  {h:>10.1e}  {dc:>16.8f}  {de:>16.8f}")
    print()


# ─────────────────────────────────────────────
#  Modo tabla de datos
# ─────────────────────────────────────────────
def cinco_puntos_tabla(puntos, x0, modo="central"):
    """
    Aplica la regla de 5 puntos sobre una tabla de puntos igualmente espaciados.
    modo: 'central' o 'extremo'
    """
    puntos_ord = sorted(puntos, key=lambda p: p[0])
    xs = [p[0] for p in puntos_ord]
    ys = [p[1] for p in puntos_ord]

    hs_difs = [xs[i+1] - xs[i] for i in range(len(xs)-1)]
    h = hs_difs[0]
    if any(abs(hi - h) > 1e-9 for hi in hs_difs):
        raise ValueError("Los puntos de la tabla deben estar igualmente espaciados para la regla de 5 puntos.")

    try:
        idx0 = next(i for i, x in enumerate(xs) if abs(x - x0) < 1e-9)
    except StopIteration:
        raise ValueError(f"x₀ = {x0} no está en la tabla.")

    titulo(f"REGLA DE 5 PUNTOS (TABLA) — {'PUNTO CENTRAL' if modo=='central' else 'PUNTO EXTREMO'}")
    print()

    if modo == "central":
        if idx0 < 2 or idx0 > len(xs) - 3:
            raise ValueError("x₀ está muy cerca del borde. Para punto central se necesitan 2 nodos a cada lado.")
        fm2 = ys[idx0-2]; fm1 = ys[idx0-1]; fp1 = ys[idx0+1]; fp2 = ys[idx0+2]
        derivada = (1/(12*h)) * (fm2 - 8*fm1 + 8*fp1 - fp2)
        nodos_idx = [idx0-2, idx0-1, idx0, idx0+1, idx0+2]
        coefs     = [1, -8, 0, 8, -1]
        formula   = "(1/12h)[ f(x₋₂) - 8f(x₋₁) + 8f(x₊₁) - f(x₊₂) ]"
    else:
        if idx0 + 4 >= len(xs):
            raise ValueError("No hay suficientes nodos a la derecha para la fórmula de punto extremo.")
        f0=ys[idx0]; f1=ys[idx0+1]; f2=ys[idx0+2]; f3=ys[idx0+3]; f4=ys[idx0+4]
        derivada = (1/(12*h)) * (-25*f0 + 48*f1 - 36*f2 + 16*f3 - 3*f4)
        nodos_idx = [idx0, idx0+1, idx0+2, idx0+3, idx0+4]
        coefs     = [-25, 48, -36, 16, -3]
        formula   = "(1/12h)[-25f(x₀) + 48f(x₁) - 36f(x₂) + 16f(x₃) - 3f(x₄)]"

    paso(1, "Tabla de datos ingresada")
    print(f"\n      {C.DIM}{'idx':>5}  {'x':>14}  {'f(x)':>14}  {'coef':>6}{C.RESET}")
    print(f"      {'─'*46}")
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i in nodos_idx:
            c = coefs[nodos_idx.index(i)]
            uso = f"{c:>6}" if c != 0 else f"{'(0)':>6}"
            marca = " ◄" if i == idx0 else "  "
            print(f"      {C.MAGENTA}{i:>5}  {x:>14.6f}  {y:>14.6f}  {uso}{marca}{C.RESET}")
        else:
            print(f"      {C.DIM}{i:>5}  {x:>14.6f}  {y:>14.6f}  {'—':>6}{C.RESET}")

    paso(2, "Fórmula aplicada")
    print(f"      {C.DIM}{formula}{C.RESET}")
    resultado("h =", f"{h:.8g}")
    resultado("f'(x₀) ≈", f"{derivada:.10g}", color=C.GREEN)

    print()
    print("─" * 66)
    print()
    return derivada


# ─────────────────────────────────────────────
#  Catálogo de funciones de ejemplo
# ─────────────────────────────────────────────
FUNCIONES = [
    {
        "nombre": "sin(x)",
        "f"     : math.sin,
        "df"    : math.cos,
        "desc"  : "Seno — f'(x) = cos(x)",
        "x0"    : 1.0,
    },
    {
        "nombre": "cos(x)",
        "f"     : math.cos,
        "df"    : lambda x: -math.sin(x),
        "desc"  : "Coseno — f'(x) = -sin(x)",
        "x0"    : 1.0,
    },
    {
        "nombre": "exp(x)",
        "f"     : math.exp,
        "df"    : math.exp,
        "desc"  : "Exponencial — f'(x) = exp(x)",
        "x0"    : 1.0,
    },
    {
        "nombre": "x⁴",
        "f"     : lambda x: x**4,
        "df"    : lambda x: 4*x**3,
        "desc"  : "Cuártica — f'(x) = 4x³",
        "x0"    : 2.0,
    },
    {
        "nombre": "ln(x)",
        "f"     : math.log,
        "df"    : lambda x: 1/x,
        "desc"  : "Logaritmo natural — f'(x) = 1/x",
        "x0"    : 2.0,
    },
    {
        "nombre": "x²·cos(x)",
        "f"     : lambda x: x**2 * math.cos(x),
        "df"    : lambda x: 2*x*math.cos(x) - x**2*math.sin(x),
        "desc"  : "x²·cos(x) — f'(x) = 2x·cos(x) - x²·sin(x)",
        "x0"    : 1.0,
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
        print(f"  {C.BLUE}[{i}]{C.RESET} {fn['nombre']:<18}  {C.DIM}{fn['desc']}{C.RESET}")
    print(f"  {C.BLUE}[{len(FUNCIONES)+1}]{C.RESET} Ingresar función personalizada")
    print()

    opcion = input("  Opción: ").strip()

    f = df = None
    nombre = ""
    x0_def = 1.0

    if opcion in [str(i) for i in range(1, len(FUNCIONES) + 2)]:
        idx = int(opcion) - 1
        if idx < len(FUNCIONES):
            fn     = FUNCIONES[idx]
            f      = fn["f"]
            df     = fn["df"]
            nombre = fn["nombre"]
            x0_def = fn["x0"]
        else:
            expr   = input("\n  f(x) en Python (usa math.sin, x**2, etc.):\n  f(x) = ").strip()
            expr_d = input("  f'(x) exacta (Enter para omitir):\n  f'(x) = ").strip()
            nombre = expr
            try:
                f = lambda x, e=expr: eval(e, {"x": x, "math": math, **vars(math)})
                f(1.0)
            except Exception as ex:
                print(f"  {C.RED}Error en f(x): {ex}{C.RESET}"); return
            df = None
            if expr_d:
                try:
                    df = lambda x, e=expr_d: eval(e, {"x": x, "math": math, **vars(math)})
                    df(1.0)
                except Exception as ex:
                    print(f"  {C.YELLOW}No se pudo evaluar f'(x): {ex}{C.RESET}")
                    df = None
    else:
        print(f"  {C.RED}Opción inválida.{C.RESET}"); return

    print()
    x0 = pedir_float(f"  x₀ (punto de evaluación) [default={x0_def}]: ", default=x0_def)
    h  = pedir_float("  h  (tamaño del paso)      [default=0.1]: ", default=0.1)

    # Mostrar ambas fórmulas paso a paso
    titulo(f"REGLA DE 5 PUNTOS — {nombre}  |  x₀={x0}, h={h}")
    mostrar_pasos_central(f, x0, h, df_exacta=df)
    print()
    mostrar_pasos_extremo(f, x0, h, df_exacta=df)
    print()

    # Comparación con 3 puntos
    comp = input("  ¿Ver comparación con la regla de 3 puntos? [s/N]: ").strip().lower()
    if comp == "s":
        comparacion(f, x0, h, df_exacta=df)

    # Convergencia
    conv = input("  ¿Ver análisis de convergencia? [s/N]: ").strip().lower()
    if conv == "s":
        analisis_convergencia(f, x0, df_exacta=df)


def menu_tabla():
    titulo("MODO: TABLA DE DATOS")
    print()
    print("  Ingresa los puntos como: x, f(x)  (uno por línea, espaciado uniforme)")
    print("  Escribe 'fin' cuando termines.\n")

    puntos = []
    while True:
        linea = input(f"  Punto {len(puntos)+1}: ").strip()
        if linea.lower() == "fin":
            break
        try:
            partes = linea.replace(";", ",").split(",")
            x = float(partes[0]); y = float(partes[1])
            puntos.append((x, y))
        except Exception:
            print(f"  {C.RED}Formato inválido. Usa: x, f(x){C.RESET}")

    if len(puntos) < 5:
        print(f"  {C.RED}Se necesitan al menos 5 puntos.{C.RESET}"); return

    print()
    x0 = pedir_float("  x₀ (debe estar en la tabla): ")
    print()
    print(f"  {C.BLUE}[1]{C.RESET} Punto central")
    print(f"  {C.BLUE}[2]{C.RESET} Punto extremo")
    modo_op = input("\n  Fórmula a usar: ").strip()
    modo = "extremo" if modo_op == "2" else "central"

    try:
        cinco_puntos_tabla(puntos, x0, modo)
    except ValueError as e:
        print(f"  {C.RED}Error: {e}{C.RESET}\n")


def ejemplo_rapido():
    titulo("EJEMPLO RÁPIDO — sin(x) en x₀=1.0, h=0.1")
    print()
    f  = math.sin
    df = math.cos
    x0 = 1.0
    h  = 0.1
    mostrar_pasos_central(f, x0, h, df_exacta=df)
    print()
    mostrar_pasos_extremo(f, x0, h, df_exacta=df)
    print()
    comparacion(f, x0, h, df_exacta=df)
    analisis_convergencia(f, x0, df_exacta=df)


def main():
    print()
    print(C.CYAN + C.BOLD + "  ╔════════════════════════════════════════════════╗" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║     REGLA DE 5 PUNTOS — DERIVACIÓN NUMÉRICA   ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ║    Punto Central  &  Punto Extremo  |  O(h⁴)  ║" + C.RESET)
    print(C.CYAN + C.BOLD + "  ╚════════════════════════════════════════════════╝" + C.RESET)

    while True:
        print()
        print(f"  {C.BOLD}Menú principal{C.RESET}")
        print(f"  {C.BLUE}[1]{C.RESET} Resolver con función f(x)")
        print(f"  {C.BLUE}[2]{C.RESET} Resolver con tabla de datos")
        print(f"  {C.BLUE}[3]{C.RESET} Ejemplo rápido (sin(x), x₀=1, h=0.1)")
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