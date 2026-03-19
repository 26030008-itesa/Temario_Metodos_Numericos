import time

def descomposicion_lu(A, b):
    n = len(A)
    
    
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    
    for i in range(n):
        L[i][i] = 1.0

   
    for i in range(n):
       
        for j in range(i, n):
            suma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - suma
            
        # Llenar la columna 'i' de la matriz L
        for j in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError(f"Cero detectado en U[{i}][{i}]. Este algoritmo de LU básico fallará sin pivoteo.")
            suma = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - suma) / U[i][i]

    # 3. Resolver Ly = b (Sustitución hacia adelante)
    y = [0.0] * n
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - suma

    # 4. Resolver Ux = y (Sustitución hacia atrás - Igual que Gauss)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ValueError("El sistema no tiene solución única.")
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]

    return x, L, U

# =================================================================
# ÁREA DE PRUEBAS
# =================================================================

if __name__ == "__main__":
    
    matriz_coeficientes = [
        [0.0,  1.0,  1.0],
        [2.0,  3.0,  1.0],
        [1.0, -1.0, -1.0]
    ]
    
    vector_resultados = [2.0, 3.0, -1.0]

    print("Calculando la solución con Descomposición LU...\n")
    
    try:
        inicio = time.perf_counter()
        
        
        solucion, matriz_L, matriz_U = descomposicion_lu(matriz_coeficientes, vector_resultados)
        
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        
        print("--- MATRIZ L (Inferior) ---")
        for fila in matriz_L:
            print(["{:.4f}".format(num) for num in fila])
            
        print("\n--- MATRIZ U (Superior) ---")
        for fila in matriz_U:
            print(["{:.4f}".format(num) for num in fila])
        
        print("\n--- SOLUCIÓN FINAL (x) ---")
        for i, valor in enumerate(solucion):
            print(f"Variable x{i+1} = {valor:.4f}")
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except ValueError as error:
        print("-" * 30)
        print(f"Error detectado: {error}")

# Calculando la solución con Descomposición LU...

# ------------------------------
# Error detectado: Cero detectado en U[0][0]. Este algoritmo de LU básico fallará sin pivoteo.
# PS C:\Users\Abram\Downloads\Tema 2\Tema_3>