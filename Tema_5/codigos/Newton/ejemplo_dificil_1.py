import time
import math

def diferencias_divididas(x, y):
    n = len(x)
    tabla = [list(y)]
    for j in range(1, n):
        col = []
        for i in range(n - j):
            col.append((tabla[j-1][i+1] - tabla[j-1][i]) / (x[i+j] - x[i]))
        tabla.append(col)
    return [tabla[j][0] for j in range(n)]

def evaluar_newton(x_datos, coef, x_eval):
    n = len(coef)
    res = coef[n-1]
    for i in range(n-2, -1, -1):
        res = res * (x_eval - x_datos[i]) + coef[i]
    return res

def error_relativo(exacto, aprox):
    return abs((exacto - aprox) / exacto) * 100 if exacto != 0 else abs(aprox)

# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # Tabla de datos: temperatura vs viscosidad del agua (valores ficticios pero reales en escala)
    # Fuente: referencia de ingeniería química
    temp    = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]   # °C
    viscos  = [1.787, 1.307, 1.002, 0.798, 0.653, 0.547, 0.467, 0.404, 0.354, 0.315]  # mPa·s

    print("=" * 65)
    print("  Newton — Caso Difícil: Interpolación de Viscosidad del Agua")
    print("=" * 65)
    print(f"  {'T (°C)':>8}  {'Viscosidad':>12}")
    print(f"  {'-'*8}  {'-'*12}")
    for t, v in zip(temp, viscos):
        print(f"  {t:>8.1f}  {v:>12.4f}")
    print("-" * 65)

    inicio = time.perf_counter()
    coef = diferencias_divididas(temp, viscos)
    fin  = time.perf_counter()
    t_coef = fin - inicio

    # Evaluar en varios puntos y comparar con valores conocidos
    puntos_eval = [15.0, 35.0, 55.0, 75.0, 85.0]
    # Valores aproximados de referencia
    referencia  = [1.139, 0.723, 0.504, 0.378, 0.334]

    print("\n  Evaluación del polinomio en puntos intermedios:")
    print(f"  {'T (°C)':>8}  {'Aprox':>12}  {'Referencia':>12}  {'Error %':>10}")
    print(f"  {'-'*8}  {'-'*12}  {'-'*12}  {'-'*10}")

    inicio2 = time.perf_counter()
    for t_e, ref in zip(puntos_eval, referencia):
        aprox = evaluar_newton(temp, coef, t_e)
        err   = error_relativo(ref, aprox)
        print(f"  {t_e:>8.1f}  {aprox:>12.6f}  {ref:>12.4f}  {err:>9.4f}%")
    fin2 = time.perf_counter()

    print("-" * 65)
    print(f"  Tiempo construcción tabla : {t_coef:.8f} s")
    print(f"  Tiempo evaluaciones       : {fin2 - inicio2:.8f} s")
    print("=" * 65)

# ====================== SALIDA ESPERADA ======================
# Los errores deben ser menores al 5% en todos los puntos
# El polinomio de grado 9 captura bien la curva de viscosidad
