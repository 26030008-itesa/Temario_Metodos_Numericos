import os
import time
import math

def ordenar_diagonal(A, b):
    """
    Intenta reordenar las filas de la matriz para acercarla a una forma diagonalmente dominante.
    """
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
        print("\n[Advertencia Matemática]")
        print("La matriz fue reordenada, pero NO cumple con la regla de la Diagonal Dominante.")
        print("Es muy probable que Jacobi diverja al infinito.\n")
    else:
        print("\n[Éxito] La matriz es estrictamente diagonalmente dominante. ¡Vía libre para iterar!\n")

    return A, b

def jacobi(A, b, max_iteraciones=1000, tolerancia=1e-4):
    n = len(b)
    
    print("Analizando y ordenando la matriz gigante (esto puede tomar un segundo)...")
    A, b = ordenar_diagonal(A, b)
    
    # 1. Lista de respuestas de la vuelta anterior
    x = [0.0] * n  
    # 2. Lista temporal para los cálculos nuevos
    x_nueva = [0.0] * n 
    
    for iteracion in range(max_iteraciones):
        error_maximo = 0.0
        
        for i in range(n):
            if A[i][i] == 0:
                raise ValueError(f"Cero en la diagonal (fila {i+1}) tras intentar reordenar.")
            
            suma = 0.0
            for j in range(n):
                if i != j:
                    # Jacobi SIEMPRE usa los valores viejos (x) para toda la vuelta
                    suma += A[i][j] * x[j]
            
            x_nueva[i] = (b[i] - suma) / A[i][i]
            
            # --- ALARMA CONTRA INCENDIOS ---
            if math.isinf(x_nueva[i]) or math.isnan(x_nueva[i]):
                raise ValueError(f"¡Explosión Matemática! Los números se fueron al infinito en la iteración {iteracion + 1}.")
            
            error_actual = abs(x_nueva[i] - x[i])
            if error_actual > error_maximo:
                error_maximo = error_actual
                
        # ACTUALIZACIÓN (Copiamos los nuevos valores para la siguiente vuelta)
        x = list(x_nueva)
        
        if error_maximo < tolerancia:
            print(f"[*] ¡El método de Jacobi convergió exitosamente en la iteración {iteracion + 1}!")
            return x
            
    raise ValueError(f"El método NO convergió después de {max_iteraciones} iteraciones.")

# =================================================================
# LECTURA DEL ARCHIVO Y RESOLUCIÓN
# =================================================================

if __name__ == "__main__":
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    directorio_padre = os.path.dirname(directorio_script)
    
    # *** AQUÍ ELIGES A QUÉ MONSTRUO ENFRENTAR ***
    # Prueba con "matriz_dominante.txt" para ver un éxito asegurado
    nombre_archivo = "matriz_dominante.txt" 
    ruta_completa = os.path.join(directorio_padre, nombre_archivo)
    
    A_leida = []
    b_leido = []
    
    try:
        with open(ruta_completa, "r") as archivo:
            for linea in archivo:
                numeros = [float(x) for x in linea.split()]
                A_leida.append(numeros[:-1])
                b_leido.append(numeros[-1])
                
        n = len(b_leido)
        print(f"¡Archivo leído! Se detectó un sistema de {n}x{n}.")
        print("Iniciando Método de Jacobi...")
        
        inicio = time.perf_counter()
        solucion = jacobi(A_leida, b_leido)
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        print("\nMuestra de la solución:")
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
        print(f"Tiempo de ejecución (hasta el colapso): {tiempo_total:.8f} segundos")

# ¡Archivo leído! Se detectó un sistema de 1000x1000.
# Iniciando Método de Jacobi...
# Analizando y ordenando la matriz gigante (esto puede tomar un segundo)...

# [Éxito] La matriz es estrictamente diagonalmente dominante. ¡Vía libre para iterar!

# [*] ¡El método de Jacobi convergió exitosamente en la iteración 3!

# Muestra de la solución:
# Variable x1 = -0.0020
# Variable x2 = -0.0016
# Variable x3 = 0.0001
# Variable x4 = 0.0006
# Variable x5 = 0.0011
# ...
# Variable x996 = -0.0016
# Variable x997 = 0.0018
# Variable x998 = -0.0017
# Variable x999 = 0.0007
# Variable x1000 = -0.0008
# ------------------------------
# Tiempo de ejecución: 0.74215870 segundos
# PS C:\Users\Abram\Downloads\Tema 2\Tema_3> 