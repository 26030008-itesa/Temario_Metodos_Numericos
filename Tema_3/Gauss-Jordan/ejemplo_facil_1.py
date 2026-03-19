import time

def gauss_jordan(A, b):
    
    n = len(b)
    M = []
    tolerancia = 1e-10 
    
  
    for i in range(n):
        fila = list(A[i])
        fila.append(b[i])
        M.append(fila)
        
   
    for i in range(n):
        
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
                
        
        if abs(M[max_row][i]) < tolerancia:
            raise ValueError(f"El sistema no tiene solución única. El pivote en la columna {i+1} es muy cercano a cero.")
            
       
        M[i], M[max_row] = M[max_row], M[i]
        
       
        pivote = M[i][i]
        for k in range(i, n + 1):
            M[i][k] /= pivote
            
       
        for j in range(n):
            if i != j:  
                factor = M[j][i]
                for k in range(i, n + 1):
                    M[j][k] -= factor * M[i][k]
                    
   
    x = [M[i][n] for i in range(n)]
        
    return x

if __name__ == "__main__":


    matriz_coeficientes = [
        [ 2.0,  1.0, -1.0],
        [-3.0, -1.0,  2.0],
        [-2.0,  1.0,  2.0]
    ]
    
    vector_resultados = [8.0, -11.0, -3.0]

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
# Variable x1 = 2.0000
# Variable x2 = 3.0000
# Variable x3 = -1.0000
# ------------------------------
# Tiempo de ejecución: 0.00003930 segundos