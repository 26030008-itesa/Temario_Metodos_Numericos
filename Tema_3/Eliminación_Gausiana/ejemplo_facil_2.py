import time
def eliminacion_gaussiana(A, b):

    n = len(b)
    
   
    M = []
    for i in range(n):
        fila = list(A[i])
        fila.append(b[i]) 
        M.append(fila)
        
   
    for i in range(n):
       
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
                
       
        if M[max_row][i] == 0:
            raise ValueError("El sistema no tiene solución única (matriz singular).")
            
       
        M[i], M[max_row] = M[max_row], M[i]
        
       
        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n + 1): 
                M[j][k] -= factor * M[i][k]
                
    
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        
        suma_productos = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - suma_productos) / M[i][i]
        
    return x



if __name__ == "__main__":
  

    matriz_coeficientes = [
        [1.0, 2.0, 3.0],
        [2.0, 4.0, 6.0],
        [3.0, 1.0, 2.0]
    ]
    
    vector_resultados = [4.0, 8.0, 5.0]

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

        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-"*30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos") 
        

#############################################################################
#        Calculando la solución...
#
#------------------------------
#        Error: El sistema no tiene solución única (matriz singular).
#        Tiempo de ejecución: 0.00003500 segundos
#################################################################################