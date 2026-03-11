import time 
import os

def eliminacion_gaussiana(A, b):

    n = len(b)
    
    # --- 1. Crear la matriz aumentada M = [A | b] ---
    M = []
    tolerancia = 1e-4
    
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
        if abs(M[max_row][i]) < tolerancia:
                raise ValueError(f"El sistema no tiene solución única. El pivote en la columna {i+1} es cero (o demasiado cercano a cero).")    
        #  
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

    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)

    nombre_archivo = "matriz_normal.txt"

    ruta_completa = os.path.join(directorio_padre, nombre_archivo)

    matriz_coeficientes = []
    vector_resultados = []
 

  

    print("Calculando la solución...\n")
    
    try:
        # 1. Leer el archivo y reconstruir las listas
        with open(ruta_completa, "r") as archivo:
            for linea in archivo:
                # Convertimos la línea de texto en una lista de números flotantes
                numeros = [float(x) for x in linea.split()]
                
                # Todos los números menos el último van a la matriz A
                matriz_coeficientes.append(numeros[:-1])
                # El último número va al vector b
                vector_resultados.append(numeros[-1])
                
        n = len(vector_resultados)
        print(f"¡Archivo leído! Se detectó un sistema de {n}x{n}.\n")
        print("Calculando la solución...")
        
        # 2. Iniciar cronómetro y resolver
        inicio = time.perf_counter()
        solucion = eliminacion_gaussiana(matriz_coeficientes, vector_resultados)
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        
        # 3. Imprimir resultados parciales para no saturar la pantalla
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