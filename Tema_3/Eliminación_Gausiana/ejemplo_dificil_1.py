import time 
import os

def eliminacion_gaussiana(A, b):

    n = len(b)
    
   
    M = []
    tolerancia = 1e-4
    
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
                raise ValueError(f"El sistema no tiene solución única. El pivote en la columna {i+1} es cero (o demasiado cercano a cero).")    
        
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

    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)

    nombre_archivo = "matriz_dominante.txt"

    ruta_completa = os.path.join(directorio_padre, nombre_archivo)

    matriz_coeficientes = []
    vector_resultados = []
 

  

    print("Calculando la solución...\n")
    
    try:
       
        with open(ruta_completa, "r") as archivo:
            for linea in archivo:
               
                numeros = [float(x) for x in linea.split()]
                
               
                matriz_coeficientes.append(numeros[:-1])
               
                vector_resultados.append(numeros[-1])
                
        n = len(vector_resultados)
        print(f"¡Archivo leído! Se detectó un sistema de {n}x{n}.\n")
        print("Calculando la solución...")
        
       
        inicio = time.perf_counter()
        solucion = eliminacion_gaussiana(matriz_coeficientes, vector_resultados)
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        
       
        print("Muestra de la solución:")
        for i in range(5):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")
        print("...")
        for i in range(n-5, n):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")

        
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Asegúrate de correr el script generador primero.")
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución (hasta fallar): {tiempo_total:.8f} segundos")

# Calculando la solución...

# ¡Archivo leído! Se detectó un sistema de 1000x1000.

# Calculando la solución...
# Muestra de la solución:
# Variable x1 = 0.0598
# Variable x2 = 1.0149
# Variable x3 = -4.1484
# Variable x4 = 0.5360
# Variable x5 = 4.9444
# ...
# Variable x996 = 4.0609
# Variable x997 = -1.1351
# Variable x998 = -2.8567
# Variable x999 = -2.4303
# Variable x1000 = -0.9848
# ------------------------------
# Tiempo de ejecución: 41.22255300 segundos