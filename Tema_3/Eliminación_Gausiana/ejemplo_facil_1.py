import time

def eliminacion_gaussiana(A, b):

    n = len(b)
    
    # --- 1. Crear la matriz aumentada M = [A | b] ---
    M = []
    for i in range(n):
        fila = list(A[i]) # Copiamos los coeficientes
        fila.append(b[i]) # Agregamos el resultado al final de la fila
        M.append(fila)
        
    # --- 2. Eliminación hacia adelante (Forward Elimination) ---
    for i in range(n):
        # Pivoteo parcial: buscar el valor absoluto mayor en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
                
        # Validar si el sistema tiene solución única
        if M[max_row][i] == 0:
            raise ValueError("El sistema no tiene solución única (matriz singular).")
            
        # Intercambiar la fila actual con la fila del pivote máximo
        M[i], M[max_row] = M[max_row], M[i]
        
        # Hacer ceros todas las entradas debajo del pivote
        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n + 1): 
                M[j][k] -= factor * M[i][k]
                
    # --- 3. Sustitución hacia atrás (Back Substitution) ---
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        # Sumar los productos de los coeficientes por las variables ya encontradas
        suma_productos = sum(M[i][j] * x[j] for j in range(i + 1, n))
        # Despejar la variable actual
        x[i] = (M[i][n] - suma_productos) / M[i][i]
        
    return x



if __name__ == "__main__":
    # Sistema de ejemplo:
    #  2x +  y -  z =   8
    # -3x -  y + 2z = -11
    # -2x +  y + 2z =  -3

    matriz_coeficientes = [
        [ 2.0,  1.0, -1.0],
        [-3.0, -1.0,  2.0],
        [-2.0,  1.0,  2.0]
    ]
    
    vector_resultados = [8.0, -11.0, -3.0]

    print("Calculando la solución...\n")
    
    try:

        inicio = time.perf_counter()

        solucion = eliminacion_gaussiana(matriz_coeficientes, vector_resultados)

        fin = time.perf_counter()

        tiempo_total = fin - inicio
        
        print("La solución del sistema es:")
        for i, valor in enumerate(solucion):
            print(f"Variable x{i+1} = {valor:.4f}")

        print("-"*30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")    
            
    except ValueError as error:
        print(f"Error: {error}")
##############################################################################
#                    La solución del sistema es:
#                    Variable x1 = 2.0000
#                    Variable x2 = 3.0000
#                    Variable x3 = -1.0000
#                    ------------------------------
#                    Tiempo de ejecución: 0.00005450 segundos
#####################################################################################