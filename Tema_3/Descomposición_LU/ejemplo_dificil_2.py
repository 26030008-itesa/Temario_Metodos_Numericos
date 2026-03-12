import os
import time

def descomposicion_lu_pivoteo(A, b):
    """
    Descomposición LU con pivoteo parcial (PLU) para sistemas robustos.
    """
    n = len(A)
    # Tolerancia para los errores de truncamiento del archivo .txt
    tolerancia = 1e-4 
    
    # 1. Inicializar matrices
    L = [[0.0] * n for _ in range(n)]
    # U empieza como una copia exacta de A
    U = [[A[i][j] for j in range(n)] for i in range(n)]
    
    # P será nuestro registro de cómo movimos las filas
    P = list(range(n))
    
    for i in range(n):
        L[i][i] = 1.0
        
    # 2. Proceso de Descomposición con Pivoteo
    for i in range(n):
        # Buscar el pivote más grande en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(U[k][i]) > abs(U[max_row][i]):
                max_row = k
                
        if abs(U[max_row][i]) < tolerancia:
            raise ValueError(f"El pivote en la columna {i+1} es muy cercano a cero. Matriz casi singular.")
            
        # Intercambiar filas en U
        U[i], U[max_row] = U[max_row], U[i]
        
        # Registrar el movimiento en P
        P[i], P[max_row] = P[max_row], P[i]
        
        # Intercambiar filas en L (SOLO los multiplicadores que ya calculamos, columnas < i)
        for k in range(i):
            L[i][k], L[max_row][k] = L[max_row][k], L[i][k]
            
        # Hacer ceros debajo del pivote en U y guardar los multiplicadores en L
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
                
    # 3. Reordenar el vector 'b' usando nuestro registro 'P'
    b_permutado = [b[P[i]] for i in range(n)]
    
    # 4. Resolver Ly = b_permutado (Sustitución hacia adelante)
    y = [0.0] * n
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b_permutado[i] - suma
        
    # 5. Resolver Ux = y (Sustitución hacia atrás)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]
        
    return x

# =================================================================
# LECTURA DEL ARCHIVO Y RESOLUCIÓN
# =================================================================

if __name__ == "__main__":
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)
    
   
    nombre_archivo = "matriz_error.txt" 
    ruta_completa = os.path.join(directorio_padre, nombre_archivo)
    
    A_leida = []
    b_leido = []
    
    print(f"Buscando el archivo en:\n{ruta_completa}\n")
    
    try:
        with open(ruta_completa, "r") as archivo:
            for linea in archivo:
                numeros = [float(x) for x in linea.split()]
                A_leida.append(numeros[:-1])
                b_leido.append(numeros[-1])
                
        n = len(b_leido)
        print(f"¡Archivo leído! Se detectó un sistema de {n}x{n}.\n")
        print("Calculando la solución con Descomposición LU (PLU)...")
        
        inicio = time.perf_counter()
        solucion = descomposicion_lu_pivoteo(A_leida, b_leido)
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        print("\nMuestra de la solución final:")
        for i in range(5):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")
        print("...")
        for i in range(n-5, n):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except FileNotFoundError:
        print(f"Error: No se encontró '{nombre_archivo}'.")
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error detectado: {error}")
        print(f"Tiempo de ejecución (hasta fallar): {tiempo_total:.8f} segundos")


# Buscando el archivo en:
# c:\Users\Abram\Downloads\Tema 2\Tema_3\matriz_error.txt

# ¡Archivo leído! Se detectó un sistema de 1000x1000.

# Calculando la solución con Descomposición LU (PLU)...
# ------------------------------
# Error detectado: El pivote en la columna 1000 es muy cercano a cero. Matriz casi singular.
# Tiempo de ejecución (hasta fallar): 36.97788460 segundos
# PS C:\Users\Abram\Downloads\Tema 2\Tema_3> 