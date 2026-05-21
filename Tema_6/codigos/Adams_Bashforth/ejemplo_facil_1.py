import time
import math

def rk4_paso(f, t, y, h):
    """Un paso de RK4 para arrancar Adams-Bashforth."""
    k1 = h * f(t,       y      )
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h,   y + k3  )
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6


def adams_bashforth_4(f, t0, y0, tf, h):
    """
    Método de Adams-Bashforth de 4 pasos (explícito).
    Fórmula:
        y_{n+1} = y_n + h/24 * (55*f_n - 59*f_{n-1} + 37*f_{n-2} - 9*f_{n-3})

    Se arrancan los primeros 3 pasos con RK4.
    """
    t_vals = [t0]
    y_vals = [y0]

    # Arranque con RK4 (necesitamos 4 puntos iniciales)
    t = t0
    y = y0
    for _ in range(3):
        y = rk4_paso(f, t, y, h)
        t = round(t + h, 10)
        t_vals.append(t)
        y_vals.append(y)

    # Fase de Adams-Bashforth de 4 pasos
    while t < tf - 1e-12:
        n = len(y_vals) - 1
        f_n   = f(t_vals[n],     y_vals[n]    )
        f_nm1 = f(t_vals[n - 1], y_vals[n - 1])
        f_nm2 = f(t_vals[n - 2], y_vals[n - 2])
        f_nm3 = f(t_vals[n - 3], y_vals[n - 3])

        y_nuevo = y_vals[n] + h/24 * (55*f_n - 59*f_nm1 + 37*f_nm2 - 9*f_nm3)
        t_nuevo = round(t + h, 10)

        t_vals.append(t_nuevo)
        y_vals.append(y_nuevo)
        t = t_nuevo

    return t_vals, y_vals


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # EDO: y' = y - t²  + 1,   y(0) = 0.5
    # Solución exacta: y(t) = (t+1)² - 0.5*e^t

    def f(t, y):
        return y - t**2 + 1

    exacta = lambda t: (t + 1)**2 - 0.5 * math.exp(t)

    t0, y0, tf = 0.0, 0.5, 4.0

    print("=" * 70)
    print("  Adams-Bashforth 4 pasos — EDO: y' = y - t² + 1,  y(0) = 0.5")
    print("  Solución exacta: y(t) = (t+1)² - 0.5·e^t")
    print("=" * 70)

    for h in [0.5, 0.1, 0.05]:
        inicio = time.perf_counter()
        t_v, y_v = adams_bashforth_4(f, t0, y0, tf, h)
        fin      = time.perf_counter()

        aprox  = y_v[-1]
        exacto = exacta(t_v[-1])
        error  = abs(aprox - exacto)

        print(f"\n  h = {h:.3f}:")
        print(f"    Pasos totales   : {len(t_v) - 1}")
        print(f"    y({t_v[-1]:.1f}) Adams-B  : {aprox:.8f}")
        print(f"    y({t_v[-1]:.1f}) exacto   : {exacto:.8f}")
        print(f"    Error absoluto  : {error:.2e}")
        print(f"    Tiempo          : {fin - inicio:.8f} s")

    print("\n  [Nota] Adams-Bashforth reutiliza evaluaciones anteriores de f,")
    print("         siendo más eficiente que RK4 en problemas con f costosa.")
    print("=" * 70)
