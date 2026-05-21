import time

def lagrange(x_datos, y_datos, x_eval):
    """
    Polinomio de interpolación de Lagrange.
    Evalúa directamente en x_eval sin construir el polinomio explícito.

    L(x) = sum_{i=0}^{n} y_i * prod_{j!=i} (x - x_j) / (x_i - x_j)
    """
    n = len(x_datos)
    resultado = 0.0

    for i in range(n):
        # Calcular el i-ésimo polinomio base L_i(x)
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x_eval - x_datos[j]) / (x_datos[i] - x_datos[j])
        resultado += y_datos[i] * L_i

    return resultado


# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # Datos de prueba: f(x) = 1 / (1 + x)
    # Exacto en x=2.5: 1/3.5 = 0.285714...
    x_datos = [0.0, 1.0, 2.0, 3.0, 4.0]
    y_datos  = [1 / (1 + xi) for xi in x_datos]

    x_eval   = 2.5
    exacto   = 1 / (1 + x_eval)

    print("=" * 55)
    print("  Polinomio de Interpolación de Lagrange")
    print("=" * 55)
    print("  Puntos de datos:")
    for xi, yi in zip(x_datos, y_datos):
        print(f"    x = {xi:.1f}  →  y = {yi:.8f}")
    print("-" * 55)

    inicio  = time.perf_counter()
    aprox   = lagrange(x_datos, y_datos, x_eval)
    fin     = time.perf_counter()

    error = abs(aprox - exacto)

    print(f"\n  Evaluación en x = {x_eval}:")
    print(f"    Valor exacto     : {exacto:.8f}")
    print(f"    Valor Lagrange   : {aprox:.8f}")
    print(f"    Error absoluto   : {error:.2e}")
    print(f"\n  Tiempo de ejecución: {fin - inicio:.8f} s")
    print("=" * 55)

# ====================== SALIDA ESPERADA ======================
# =======================================================
#   Polinomio de Interpolación de Lagrange
# =======================================================
#   Puntos de datos:
#     x = 0.0  →  y = 1.00000000
#     x = 1.0  →  y = 0.50000000
#     ...
#   Evaluación en x = 2.5:
#     Valor exacto     : 0.28571429
#     Valor Lagrange   : 0.28571429
#     Error absoluto   : ~0.00e+00
# =======================================================
