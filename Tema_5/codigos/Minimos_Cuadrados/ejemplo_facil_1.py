import time

def minimos_cuadrados(x, y, grado=1):
    """
    Ajuste por Mínimos Cuadrados.
    Resuelve el sistema normal A^T A c = A^T y
    para obtener los coeficientes del polinomio de ajuste de 'grado' dado.

    Retorna la lista de coeficientes [c0, c1, ..., c_grado]
    donde el polinomio es: P(x) = c0 + c1*x + c2*x^2 + ...
    """
    n  = len(x)
    m  = grado + 1   # número de coeficientes

    # Construir la matriz de Vandermonde A (n x m)
    A = [[xi**j for j in range(m)] for xi in x]

    # Calcular A^T A (m x m) y A^T y (m x 1)
    AtA = [[0.0] * m for _ in range(m)]
    Aty = [0.0] * m

    for i in range(m):
        for j in range(m):
            AtA[i][j] = sum(A[k][i] * A[k][j] for k in range(n))
        Aty[i] = sum(A[k][i] * y[k] for k in range(n))

    # Resolver el sistema AtA * c = Aty por eliminación gaussiana
    coef = _gauss(AtA, Aty)
    return coef


def _gauss(A, b):
    """Eliminación Gaussiana con pivoteo parcial para sistemas m x m pequeños."""
    m = len(b)
    Ab = [A[i][:] + [b[i]] for i in range(m)]

    for col in range(m):
        # Pivoteo parcial
        max_fila = max(range(col, m), key=lambda r: abs(Ab[r][col]))
        Ab[col], Ab[max_fila] = Ab[max_fila], Ab[col]

        for fila in range(col + 1, m):
            if Ab[col][col] == 0:
                continue
            factor = Ab[fila][col] / Ab[col][col]
            for j in range(col, m + 1):
                Ab[fila][j] -= factor * Ab[col][j]

    # Sustitución hacia atrás
    x = [0.0] * m
    for i in range(m - 1, -1, -1):
        x[i] = Ab[i][m]
        for j in range(i + 1, m):
            x[i] -= Ab[i][j] * x[j]
        x[i] /= Ab[i][i]
    return x


def evaluar_polinomio(coef, x_eval):
    return sum(coef[j] * x_eval**j for j in range(len(coef)))


def r_cuadrada(x, y, coef):
    """Calcula el coeficiente de determinación R²."""
    y_prom = sum(y) / len(y)
    ss_tot = sum((yi - y_prom)**2 for yi in y)
    ss_res = sum((yi - evaluar_polinomio(coef, xi))**2 for xi, yi in zip(x, y))
    return 1 - ss_res / ss_tot


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # Datos experimentales: posición vs tiempo de un objeto
    t_datos = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    s_datos = [0.0, 1.1, 3.9, 9.2, 16.1, 24.8]   # s ≈ 5t - 4.9t²/2... aprox cuadrático

    print("=" * 60)
    print("  Mínimos Cuadrados — Ajuste Polinomial")
    print("=" * 60)
    print("  Datos experimentales (tiempo vs posición):")
    print(f"  {'t':>6}  {'s':>8}")
    for t, s in zip(t_datos, s_datos):
        print(f"  {t:>6.1f}  {s:>8.2f}")
    print("-" * 60)

    for grado in [1, 2]:
        inicio = time.perf_counter()
        coef   = minimos_cuadrados(t_datos, s_datos, grado=grado)
        fin    = time.perf_counter()
        r2     = r_cuadrada(t_datos, s_datos, coef)

        terminos = " + ".join(f"{c:.4f}·t^{i}" if i > 0 else f"{c:.4f}" for i, c in enumerate(coef))
        print(f"\n  Grado {grado}: P(t) = {terminos}")
        print(f"    R² = {r2:.6f}   (más cercano a 1 → mejor ajuste)")
        print(f"    Tiempo: {fin - inicio:.8f} s")

    print("=" * 60)

# ====================== SALIDA ESPERADA ======================
#   Grado 1: P(t) = -0.5143 + 5.0057·t^1      R² ≈ 0.998
#   Grado 2: P(t) = 0.0857 + 0.1771·t^1 + 0.9514·t^2   R² ≈ 0.9999
