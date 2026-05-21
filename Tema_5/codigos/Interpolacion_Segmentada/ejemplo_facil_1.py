import time

def spline_cubico_natural(x, y):
    """
    Calcula los coeficientes del Spline Cúbico Natural.
    Condiciones de frontera: S''(x0) = S''(xn) = 0

    Retorna listas a, b, c, d para cada segmento i tal que:
        S_i(x) = a[i] + b[i](x-x_i) + c[i](x-x_i)² + d[i](x-x_i)³
    """
    n = len(x) - 1   # número de segmentos
    h = [x[i+1] - x[i] for i in range(n)]

    # Construir el sistema tridiagonal para los c[i] (momentos)
    alpha = [0.0] * (n + 1)
    for i in range(1, n):
        alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])

    # Algoritmo de Thomas (tridiagonal)
    l  = [1.0] + [0.0] * n
    mu = [0.0] * (n + 1)
    z  = [0.0] * (n + 1)

    for i in range(1, n):
        l[i]  = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i] / l[i]
        z[i]  = (alpha[i] - h[i-1]*z[i-1]) / l[i]

    l[n] = 1.0

    c = [0.0] * (n + 1)
    b = [0.0] * n
    d = [0.0] * n

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (y[j+1] - y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    a = list(y[:-1])
    return a, b, c, d


def evaluar_spline(x_datos, a, b, c, d, x_eval):
    """Evalúa el spline en x_eval buscando el segmento correcto."""
    n = len(a)
    # Buscar el índice del segmento que contiene x_eval
    idx = 0
    for i in range(n - 1):
        if x_datos[i] <= x_eval <= x_datos[i+1]:
            idx = i
            break
    else:
        idx = n - 1   # extrapolación (último segmento)

    dx = x_eval - x_datos[idx]
    return a[idx] + b[idx]*dx + c[idx]*dx**2 + d[idx]*dx**3


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    import math

    # Puntos de f(x) = cos(x)
    x_datos = [0.0, 0.5, 1.0, 1.5, 2.0]
    y_datos  = [math.cos(xi) for xi in x_datos]

    print("=" * 60)
    print("  Interpolación Segmentada — Spline Cúbico Natural")
    print("=" * 60)
    print("  Puntos de interpolación (f(x) = cos(x)):")
    for xi, yi in zip(x_datos, y_datos):
        print(f"    x = {xi:.2f}  →  cos(x) = {yi:.6f}")
    print("-" * 60)

    inicio = time.perf_counter()
    a, b, c, d = spline_cubico_natural(x_datos, y_datos)
    fin = time.perf_counter()

    print("\n  Evaluación del Spline vs. cos(x) exacto:")
    print(f"  {'x_eval':>8}  {'Spline':>12}  {'Exacto':>12}  {'Error':>12}")
    print(f"  {'-'*8}  {'-'*12}  {'-'*12}  {'-'*12}")

    puntos = [0.25, 0.75, 1.25, 1.75]
    for xp in puntos:
        aprox  = evaluar_spline(x_datos, a, b, c, d, xp)
        exacto = math.cos(xp)
        error  = abs(aprox - exacto)
        print(f"  {xp:>8.2f}  {aprox:>12.8f}  {exacto:>12.8f}  {error:>12.2e}")

    print(f"\n  Tiempo construcción spline: {fin - inicio:.8f} s")
    print("=" * 60)
