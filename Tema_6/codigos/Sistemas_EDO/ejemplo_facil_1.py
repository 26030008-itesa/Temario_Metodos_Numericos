import time
import math

def rk4_sistema(F, t0, Y0, tf, h):
    """
    Runge-Kutta 4 para un **sistema** de EDOs.
        Y' = F(t, Y),   Y = [y1, y2, ..., yn]

    Parámetros:
        F   : función que recibe (t, Y) y devuelve lista [f1, f2, ..., fn]
        t0  : tiempo inicial
        Y0  : lista de condiciones iniciales [y1(t0), y2(t0), ...]
        tf  : tiempo final
        h   : tamaño del paso

    Retorna:
        t_vals : lista de tiempos
        Y_vals : lista de vectores de estado
    """
    def sumar(a, b, escala=1.0):
        return [ai + escala * bi for ai, bi in zip(a, b)]

    t_vals = [t0]
    Y_vals = [list(Y0)]

    t = t0
    Y = list(Y0)
    n = len(Y)

    while t < tf - 1e-12:
        K1 = F(t,         Y                    )
        K2 = F(t + h/2,   sumar(Y, K1, h/2)   )
        K3 = F(t + h/2,   sumar(Y, K2, h/2)   )
        K4 = F(t + h,     sumar(Y, K3, h)      )

        Y = [Y[i] + h/6 * (K1[i] + 2*K2[i] + 2*K3[i] + K4[i]) for i in range(n)]
        t = round(t + h, 10)

        t_vals.append(t)
        Y_vals.append(list(Y))

    return t_vals, Y_vals


# =================================================================
# ÁREA DE PRUEBAS — Péndulo Simple (no lineal)
# =================================================================

if __name__ == "__main__":
    # Sistema:  θ'' + (g/L)*sin(θ) = 0
    # Variables: y1 = θ (ángulo),  y2 = θ' (velocidad angular)
    # EDOs:
    #   y1' = y2
    #   y2' = -(g/L) * sin(y1)

    g = 9.81   # m/s²
    L = 1.0    # m (longitud del péndulo)

    def F(t, Y):
        theta, omega = Y
        return [omega, -(g / L) * math.sin(theta)]

    # Condiciones iniciales: ángulo inicial 30°, velocidad angular 0
    theta0 = math.radians(30)   # 30° en radianes
    omega0 = 0.0

    t0, tf = 0.0, 10.0
    h      = 0.01

    print("=" * 65)
    print("  Sistema de EDOs — Péndulo Simple No Lineal")
    print(f"  g = {g} m/s²,  L = {L} m")
    print(f"  θ(0) = 30°,  θ'(0) = 0  →  tf = {tf} s,  h = {h}")
    print("=" * 65)

    inicio = time.perf_counter()
    t_vals, Y_vals = rk4_sistema(F, t0, [theta0, omega0], tf, h)
    fin    = time.perf_counter()

    # Período analítico (pequeña oscilación): T = 2π√(L/g)
    T_analitico = 2 * math.pi * math.sqrt(L / g)

    # Buscar el primer cruce por cero después de t0 (semi-período)
    semi_T_num = None
    for i in range(1, len(t_vals)):
        if Y_vals[i-1][0] > 0 and Y_vals[i][0] <= 0:
            semi_T_num = t_vals[i]
            break

    print(f"\n  Pasos calculados     : {len(t_vals) - 1}")
    print(f"  Tiempo de ejecución  : {fin - inicio:.4f} s")
    print(f"\n  Período analítico (pequeña oscilación): {T_analitico:.4f} s")
    if semi_T_num:
        print(f"  Primer semi-período numérico (θ→0)   : ~{semi_T_num:.4f} s")
        print(f"  (El período numérico completo es mayor que el analítico")
        print(f"   para ángulos grandes — efecto no lineal de sin(θ))")

    print("\n  Estado final (t=10s):")
    print(f"    θ  = {math.degrees(Y_vals[-1][0]):>10.4f} °")
    print(f"    θ' = {Y_vals[-1][1]:>10.4f} rad/s")
    print("=" * 65)

# ====================== SALIDA ESPERADA ======================
#   Período analítico ≈ 2.0064 s
#   Período numérico  ≈ 2.02 s  (ligeramente mayor por no-linealidad a 30°)
