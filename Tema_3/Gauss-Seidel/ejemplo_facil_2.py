import time

def ordenar_diagonal(A, b):
    """
    Intenta reordenar las filas de la matriz para que sea diagonalmente dominante,
    colocando el valor absoluto más grande de cada columna en la diagonal.
    """
    n = len(b)
    for i in range(n):
        # Buscar la fila (desde i hasta n) con el valor absoluto más grande en la columna i
        max_row = i
        for k in range(i, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
                
        # Intercambiar la fila actual con la mejor fila encontrada
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
    # --- Verificación de Seguridad ---
    es_dominante = True
    for i in range(n):
        # Sumar todos los números de la fila (excepto el de la diagonal)
        suma_restantes = sum(abs(A[i][j]) for j in range(n) if i != j)
        
        if abs(A[i][i]) <= suma_restantes:
            es_dominante = False
            break
            
    if not es_dominante:
        print("[Advertencia] Se reordenó la matriz, pero matemáticamente NO se pudo hacer estrictamente diagonalmente dominante.")
        print("Es muy probable que el método no converja.\n")
    else:
        print("[Éxito] La matriz fue reordenada automáticamente y es diagonalmente dominante.\n")

    return A, b

def gauss_seidel(A, b, max_iteraciones=1000, tolerancia=1e-6):
    n = len(b)
    
    # 1. ¡Llamamos a nuestro auto-corrector antes de empezar!
    A, b = ordenar_diagonal(A, b)
    
    x = [0.0] * n  
    
    for iteracion in range(max_iteraciones):
        error_maximo = 0.0
        
        for i in range(n):
            x_viejo = x[i]
            
            if A[i][i] == 0:
                raise ValueError(f"Cero en la diagonal (fila {i+1}) tras intentar reordenar.")
            
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            
            x[i] = (b[i] - suma) / A[i][i]
            error_actual = abs(x[i] - x_viejo)
            
            if error_actual > error_maximo:
                error_maximo = error_actual
                
        if error_maximo < tolerancia:
            print(f"[*] El método convergió exitosamente en la iteración {iteracion + 1}.")
            return x
            
    raise ValueError(f"El método NO convergió después de {max_iteraciones} iteraciones.")

# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    matriz_coeficientes = [
        [1.0, 2.0, 3.0],
        [2.0, 4.0, 6.0],
        [3.0, 1.0, 2.0]
    ]
    
    vector_resultados = [4.0, 8.0, 5.0]

    print("Calculando la solución con Gauss-Seidel...\n")
    
    try:
        inicio = time.perf_counter()
        solucion = gauss_seidel(matriz_coeficientes, vector_resultados)
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        print("\nLa solución del sistema es:")
        for i, valor in enumerate(solucion):
            print(f"Variable x{i+1} = {valor:.6f}")
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución (hasta detenerse): {tiempo_total:.8f} segundos")


# Calculando la solución con Gauss-Seidel...

# [Advertencia] Se reordenó la matriz, pero matemáticamente NO se pudo hacer estrictamente diagonalmente dominante.
# Es muy probable que el método no converja.

# [*] El método convergió exitosamente en la iteración 10.

# La solución del sistema es:
# Variable x1 = 1.200000
# Variable x2 = 1.400000
# Variable x3 = 0.000000
# ------------------------------
# Tiempo de ejecución: 0.00041160 segundos