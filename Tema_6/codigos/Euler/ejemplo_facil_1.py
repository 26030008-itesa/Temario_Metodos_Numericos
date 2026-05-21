import time

def euler(f, t0, y0, tf, h):
    """
    Método de Euler (un paso) para resolver y' = f(t, y).

    Parámetros:
        f   : función f(t, y) que define la EDO
        t0  : tiempo inicial
        y0  : condición inicial y(t0)
        tf  : tiempo final
        h   : tamaño del paso

    Retorna:
        t_vals : lista de tiempos
        y_vals : lista de valores aproximados de y
    """
    t_vals = [t0]
    y_vals = [y0]

    t = t0
    y = y0

    while t < tf - 1e-12:   # 1e-12 para evitar error de punto flotante
        y = y + h * f(t, y)
        t = t + h
        t_vals.append(round(t, 10))
        y_vals.append(y)

    return t_vals, y_vals


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    import math

    # EDO: y' = -2y,   y(0) = 1
    # Solución exacta: y(t) = e^(-2t)

    def f(t, y):
        return -2 * y

    t0, y0, tf = 0.0, 1.0, 2.0
    exacta = lambda t: math.exp(-2 * t)

    print("=" * 65)
    print("  Método de Euler — EDO: y' = -2y,  y(0) = 1")
    print("  Solución exacta: y(t) = e^(-2t)")
    print("=" * 65)

    for h in [0.5, 0.1, 0.01]:
        inicio = time.perf_counter()
        t_vals, y_vals = euler(f, t0, y0, tf, h)
        fin    = time.perf_counter()

        # Error en el tiempo final
        y_aprox = y_vals[-1]
        y_exact = exacta(tf)
        error   = abs(y_aprox - y_exact)

        print(f"\n  h = {h:.3f}:")
        print(f"    Pasos realizados : {len(t_vals) - 1}")
        print(f"    y({tf}) aproximado: {y_aprox:.8f}")
        print(f"    y({tf}) exacto    : {y_exact:.8f}")
        print(f"    Error absoluto   : {error:.2e}")
        print(f"    Tiempo           : {fin - inicio:.8f} s")

    print("\n  [Nota] Al reducir h a la mitad, el error se reduce a la mitad → O(h)")
    print("=" * 65)

# ====================== SALIDA ESPERADA ======================
#   h = 0.500:  error ~ 3e-2
#   h = 0.100:  error ~ 6e-3
#   h = 0.010:  error ~ 6e-4   (orden lineal en h)
