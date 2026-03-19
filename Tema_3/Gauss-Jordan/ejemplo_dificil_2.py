import os
import time

def gauss_jordan(A, b):
    """
    Resuelve un sistema Ax = b usando Gauss-Jordan con pivoteo parcial.
    Adaptado con tolerancia para lectura de archivos grandes.
    """
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
        print("Calculando la solución con Gauss-Jordan...")
        
      
        inicio = time.perf_counter()
        solucion = gauss_jordan(A_leida, b_leido)
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
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Revisa que esté en Tema_3.")
    except ValueError as error:
        fin = time.perf_counter()
        tiempo_total = fin - inicio
        print("-" * 30)
        print(f"Error: {error}")
        print(f"Tiempo de ejecución (hasta fallar): {tiempo_total:.8f} segundos")





# ¡Archivo leído! Se detectó un sistema de 1000x1000.

# Calculando la solución con Gauss-Jordan...
# ------------------------------
# Error: El sistema no tiene solución única. El pivote en la columna 1000 es muy cercano a cero.
# Tiempo de ejecución (hasta fallar): 55.86091170 segundos