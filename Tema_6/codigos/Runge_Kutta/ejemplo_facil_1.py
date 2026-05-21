import time

def runge_kutta_4(f, t0, y0, tf, h):
    """
    Método de Runge-Kutta de orden 4 (RK4) para y' = f(t, y).

    En cada paso calcula 4 pendientes:
        k1 = h * f(t,        y           )
        k2 = h * f(t + h/2,  y + k1/2    )
        k3 = h * f(t + h/2,  y + k2/2    )
        k4 = h * f(t + h,    y + k3      )
        y_nuevo = y + (k1 + 2k2 + 2k3 + k4) / 6

    Retorna:
        t_vals : lista de tiempos
        y_vals : lista de valores aproximados
    """
    t_vals = [t0]
    y_vals = [y0]

    t = t0
    y = y0

    while t < tf - 1e-12:
        k1 = h * f(t,         y         )
        k2 = h * f(t + h/2,   y + k1/2  )
        k3 = h * f(t + h/2,   y + k2/2  )
        k4 = h * f(t + h,     y + k3    )

        y  = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t  = t + h

        t_vals.append(round(t, 10))
        y_vals.append(y)

    return t_vals, y_vals


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    import math

    # EDO: y' = t*y + t^3,   y(0) = 1
    # Solución exacta: y(t) = 3*e^(t²/2) - t² - 2

    def f(t, y):
        return t * y + t**3

    exacta = lambda t: 3 * math.exp(t**2 / 2) - t**2 - 2

    t0, y0, tf = 0.0, 1.0, 2.0

    print("=" * 65)
    print("  Runge-Kutta 4 — EDO: y' = t·y + t³,  y(0) = 1")
    print("  Solución exacta: y(t) = 3·e^(t²/2) - t² - 2")
    print("=" * 65)
    print(f"  {'h':>8}  {'y(2.0) RK4':>14}  {'y(2.0) exacto':>14}  {'Error':>12}  {'Tiempo':>12}")
    print(f"  {'-'*8}  {'-'*14}  {'-'*14}  {'-'*12}  {'-'*12}")

    for h in [0.5, 0.25, 0.1, 0.05]:
        inicio = time.perf_counter()
        t_v, y_v = runge_kutta_4(f, t0, y0, tf, h)
        fin      = time.perf_counter()

        aprox  = y_v[-1]
        exacto = exacta(tf)
        error  = abs(aprox - exacto)

        print(f"  {h:>8.3f}  {aprox:>14.8f}  {exacto:>14.8f}  {error:>12.2e}  {fin-inicio:>12.8f}")

    print("\n  [Nota] Al reducir h a la mitad, el error se reduce 16 veces → O(h⁴)")
    print("=" * 65)

# ====================== SALIDA ESPERADA ======================
#   h = 0.500: error ~ 5e-2
#   h = 0.250: error ~ 3e-3
#   h = 0.100: error ~ 1e-4   (orden cuártico en h)
