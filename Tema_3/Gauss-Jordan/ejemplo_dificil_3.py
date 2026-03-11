import os
import time

def gauss_jordan(A, b):
    """
    Resuelve un sistema Ax = b usando Gauss-Jordan con pivoteo parcial.
    Adaptado con tolerancia para lectura de archivos grandes.
    """
    n = len(b)
    M = []
    
    # Tolerancia ajustada para los errores de redondeo al guardar en .txt (6 decimales)
    tolerancia = 1e-4  
    
    # --- 1. Crear matriz aumentada ---
    for i in range(n):
        fila = list(A[i])
        fila.append(b[i])
        M.append(fila)
        
    # --- 2. Eliminación Gauss-Jordan ---
    for i in range(n):
        # Pivoteo parcial
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
                
        # Validar matriz singular con la tolerancia
        if abs(M[max_row][i]) < tolerancia:
            raise ValueError(f"El sistema no tiene solución única. El pivote en la columna {i+1} es muy cercano a cero.")
            
        M[i], M[max_row] = M[max_row], M[i]
        
        # Convertir el pivote en 1
        pivote = M[i][i]
        for k in range(i, n + 1):
            M[i][k] /= pivote
            
        # Hacer ceros ARRIBA y ABAJO del pivote
        for j in range(n):
            if i != j:
                factor = M[j][i]
                for k in range(i, n + 1):
                    M[j][k] -= factor * M[i][k]
                    
    # --- 3. Extraer la solución directamente de la última columna ---
    x = [M[i][n] for i in range(n)]
        
    return x

# =================================================================
# LECTURA DEL ARCHIVO Y RESOLUCIÓN
# =================================================================

if __name__ == "__main__":
    # 1. Rutas automáticas hacia la carpeta Tema_3
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)
    
    # *** CAMBIA ESTE NOMBRE PARA PROBAR LOS DISTINTOS CASOS ***
    nombre_archivo = "matriz_dominante_desordenada.txt" 
    
    ruta_completa = os.path.join(directorio_padre, nombre_archivo)
    
    A_leida = []
    b_leido = []
    
    print(f"Buscando el archivo en:\n{ruta_completa}\n")
    
    try:
        # 2. Leer la matriz gigante
        with open(ruta_completa, "r") as archivo:
            for linea in archivo:
                numeros = [float(x) for x in linea.split()]
                A_leida.append(numeros[:-1])
                b_leido.append(numeros[-1])
                
        n = len(b_leido)
        print(f"¡Archivo leído! Se detectó un sistema de {n}x{n}.\n")
        print("Calculando la solución con Gauss-Jordan...")
        
        # 3. Iniciar cronómetro y resolver
        inicio = time.perf_counter()
        solucion = gauss_jordan(A_leida, b_leido)
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        # 4. Imprimir resultados (Solo los primeros 5 y los últimos 5)
        print("\nMuestra de la solución:")
        for i in range(5):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")
        print("...")
        for i in range(n-5, n):
            print(f"Variable x{i+1} = {solucion[i]:.4f}")
            
        print("-" * 30)
        print(f"Tiempo de ejecución: {tiempo_total:.8f} segundos")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Revisa que esté en Tema_3.")
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución (hasta fallar): {tiempo_total:.8f} segundos")


# ¡Archivo leído! Se detectó un sistema de 1000x1000.

# Calculando la solución con Gauss-Jordan...

# Muestra de la solución:
# Variable x1 = 0.9832
# Variable x2 = -2.2567
# Variable x3 = 2.4610
# Variable x4 = 1.4385
# Variable x5 = -0.2403
# ...
# Variable x996 = -0.4956
# Variable x997 = -0.3388
# Variable x998 = -1.0961
# Variable x999 = -0.6473
# Variable x1000 = -3.3818
# ------------------------------
# Tiempo de ejecución: 54.11300050 segundos
# PS C:\Users\Abram\Downloads\Tema 2\Tema_3> 



#### Matriz dominante



# ¡Archivo leído! Se detectó un sistema de 1000x1000.

# Calculando la solución con Gauss-Jordan...

# Muestra de la solución:
# Variable x1 = 0.0005
# Variable x2 = -0.0008
# Variable x3 = -0.0010
# Variable x4 = 0.0007
# Variable x5 = -0.0005
# ...
# Variable x996 = -0.0017
# Variable x997 = 0.0011
# Variable x998 = 0.0011
# Variable x999 = -0.0001
# Variable x1000 = -0.0002
# ------------------------------
# Tiempo de ejecución: 56.42411010 segundos
# PS C:\Users\Abram\Downloads\Tema 2\Tema_3> 





