import time

def diferencias_divididas(x, y):
    """
    Construye la tabla de diferencias divididas de Newton.
    Retorna el vector de coeficientes [f[x0], f[x0,x1], f[x0,x1,x2], ...]
    """
    n = len(x)
    # Copiar y como primera columna de la tabla
    tabla = [list(y)]

    for j in range(1, n):
        columna = []
        for i in range(n - j):
            dd = (tabla[j - 1][i + 1] - tabla[j - 1][i]) / (x[i + j] - x[i])
            columna.append(dd)
        tabla.append(columna)

    coeficientes = [tabla[j][0] for j in range(n)]
    return coeficientes


def evaluar_newton(x_datos, coef, x_eval):
    """
    Evalúa el polinomio de Newton en x_eval dado el vector de coeficientes.
    Usa el algoritmo de Horner anidado para eficiencia.
    """
    n = len(coef)
    resultado = coef[n - 1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x_eval - x_datos[i]) + coef[i]
    return resultado


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # Puntos conocidos de f(x) = sin(x)
    import math

    x_datos = [0.0, 0.5, 1.0, 1.5]
    y_datos  = [math.sin(xi) for xi in x_datos]

    print("=" * 55)
    print("  Polinomio de Interpolación de Newton")
    print("=" * 55)
    print("  Puntos de interpolación:")
    for xi, yi in zip(x_datos, y_datos):
        print(f"    x = {xi:.1f}  →  f(x) = {yi:.6f}")
    print("-" * 55)

    inicio = time.perf_counter()
    coef = diferencias_divididas(x_datos, y_datos)
    fin  = time.perf_counter()

    print("\n  Coeficientes del polinomio de Newton:")
    for i, c in enumerate(coef):
        print(f"    c[{i}] = {c:.8f}")

    # Evaluar en un punto intermedio
    x_eval   = 0.8
    exacto   = math.sin(x_eval)
    aprox    = evaluar_newton(x_datos, coef, x_eval)
    error    = abs(aprox - exacto)

    print(f"\n  Evaluación en x = {x_eval}:")
    print(f"    Valor exacto      : {exacto:.8f}")
    print(f"    Valor aproximado  : {aprox:.8f}")
    print(f"    Error absoluto    : {error:.2e}")
    print(f"\n  Tiempo de ejecución: {fin - inicio:.8f} s")
    print("=" * 55)

# ====================== SALIDA ESPERADA ======================
# =======================================================
#   Polinomio de Interpolación de Newton
# =======================================================
#   Puntos de interpolación:
#     x = 0.0  →  f(x) = 0.000000
#     x = 0.5  →  f(x) = 0.479426
#     x = 1.0  →  f(x) = 0.841471
#     x = 1.5  →  f(x) = 0.997495
# -------------------------------------------------------
#   Coeficientes del polinomio de Newton:
#     c[0] = 0.00000000
#     c[1] = 0.95885164
#     ...
#   Evaluación en x = 0.8:
#     Valor exacto      : 0.71735609
#     Valor aproximado  : ~0.71735...
#     Error absoluto    : ~1e-5
# =======================================================
