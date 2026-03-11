import time
import math

def ordenar_diagonal(A, b):
    n = len(b)
    for i in range(n):
        max_row = i
        for k in range(i, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
    es_dominante = True
    for i in range(n):
        suma_restantes = sum(abs(A[i][j]) for j in range(n) if i != j)
        if abs(A[i][i]) <= suma_restantes:
            es_dominante = False
            break
            
    if not es_dominante:
        print("[Advertencia] Se reordenó la matriz, pero NO es estrictamente diagonalmente dominante.")
        print("Es muy probable que Jacobi diverja al infinito.\n")
    else:
        print("[Éxito] La matriz fue reordenada y es diagonalmente dominante.\n")

    return A, b

def jacobi(A, b, max_iteraciones=1000, tolerancia=1e-6):
    n = len(b)
    
    # 1. Intentamos salvar la matriz antes de empezar
    A, b = ordenar_diagonal(A, b)
    
    x = [0.0] * n  
    x_nueva = [0.0] * n 
    
    for iteracion in range(max_iteraciones):
        error_maximo = 0.0
        
        for i in range(n):
            if A[i][i] == 0:
                raise ValueError(f"Cero en la diagonal (fila {i+1}). Jacobi fallará.")
            
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            
            x_nueva[i] = (b[i] - suma) / A[i][i]
            
            # Alarma contra infinitos
            if math.isinf(x_nueva[i]) or math.isnan(x_nueva[i]):
                raise ValueError(f"¡Explosión Matemática! Los números se fueron al infinito en la iteración {iteracion + 1}.")
            
            error_actual = abs(x_nueva[i] - x[i])
            if error_actual > error_maximo:
                error_maximo = error_actual
                
        # Actualizamos todos los valores a la vez (La diferencia clave de Jacobi)
        x = list(x_nueva)
        
        if error_maximo < tolerancia:
            print(f"[*] El método de Jacobi convergió en la iteración {iteracion + 1}.")
            return x
            
    raise ValueError(f"El método NO convergió después de {max_iteraciones} iteraciones.")

# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    # Matriz del ejercicio (Singular - Sin solución)
    matriz_coeficientes = [
        [ 2.0,  1.0, -1.0],
        [-3.0, -1.0,  2.0],
        [-2.0,  1.0,  2.0]
    ]
    
    vector_resultados = [8.0, -11.0, -3.0]

    print("Calculando la solución con el método de Jacobi...\n")
    
    try:
        inicio = time.perf_counter()
        solucion = jacobi(matriz_coeficientes, vector_resultados)
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
        print(f"Error detectado: {error}")
        print(f"Tiempo de ejecución (hasta detenerse): {tiempo_total:.8f} segundos")

# Calculando la solución con el método de Jacobi...

# [Advertencia] Se reordenó la matriz, pero NO es estrictamente diagonalmente dominante.
# Es muy probable que Jacobi diverja al infinito.

# ------------------------------
# Error detectado: El método NO convergió después de 1000 iteraciones.
# Tiempo de ejecución (hasta detenerse): 0.00324410 segundos