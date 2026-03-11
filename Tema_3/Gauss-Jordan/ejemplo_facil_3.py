import time

def gauss_jordan(A, b):
    
    n = len(b)
    M = []
    tolerancia = 1e-10  # Mantenemos nuestra defensa contra decimales basura
    
    # --- 1. Crear la matriz aumentada M = [A | b] ---
    for i in range(n):
        fila = list(A[i])
        fila.append(b[i])
        M.append(fila)
        
    # --- 2. Proceso de Gauss-Jordan ---
    for i in range(n):
        # Pivoteo parcial (Igual que en Gauss)
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
                
        # Validación de matriz singular con tolerancia
        if abs(M[max_row][i]) < tolerancia:
            raise ValueError(f"El sistema no tiene solución única. El pivote en la columna {i+1} es muy cercano a cero.")
            
        # Intercambiar la fila actual con la fila del pivote
        M[i], M[max_row] = M[max_row], M[i]
        
        # a) Convertir el pivote actual en 1 (Dividiendo toda la fila entre el pivote)
        pivote = M[i][i]
        for k in range(i, n + 1):
            M[i][k] /= pivote
            
        # b) Hacer ceros ARRIBA y ABAJO del pivote
        for j in range(n):
            if i != j:  # Si no es la fila del pivote actual
                factor = M[j][i]
                for k in range(i, n + 1):
                    M[j][k] -= factor * M[i][k]
                    
    # --- 3. Extraer la solución ---
    # Como la matriz ahora es una diagonal de 1s, la última columna ES la solución.
    # Ya no necesitamos el bloque de "Sustitución hacia atrás"
    x = [M[i][n] for i in range(n)]
        
    return x

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

    print("Calculando la solución con Gauss-Jordan...\n")
    
    try:
        inicio = time.perf_counter()
        solucion = gauss_jordan(matriz_coeficientes, vector_resultados)
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        print("La solución del sistema es:")
        for i, valor in enumerate(solucion):
            print(f"Variable x{i+1} = {valor:.4f}")
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución (hasta fallar): {tiempo_total:.8f} segundos")



# Calculando la solución con Gauss-Jordan...

# La solución del sistema es:
# Variable x1 = 1.0000
# Variable x2 = -0.5000
# Variable x3 = 2.5000
# ------------------------------
# Tiempo de ejecución: 0.00003130 segundos
