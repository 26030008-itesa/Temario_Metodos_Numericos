import random

def guardar_matriz(matriz, vector, nombre_archivo):
    """
    Toma una matriz A y un vector b, los une y los guarda en un archivo txt.
    """
    with open(nombre_archivo, "w") as archivo:
        for i in range(len(matriz)):
            # Unimos los coeficientes con su resultado correspondiente
            fila_completa = matriz[i] + [vector[i]]
            # Formateamos a 6 decimales y separamos por espacios
            linea_texto = " ".join([f"{num:10.6f}" for num in fila_completa])
            archivo.write(linea_texto + "\n")
    print(f"[*] Archivo creado exitosamente: {nombre_archivo}")

def generar_casos_prueba(n):
    print(f"Generando los 3 casos de prueba para sistemas de {n}x{n}...\n")

    # ---------------------------------------------------------
    # CASO 1: NORMAL (Converge sin problemas)
    # ---------------------------------------------------------
    A_normal = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_normal = [random.uniform(-10, 10) for _ in range(n)]
    guardar_matriz(A_normal, b_normal, "matriz_normal.txt")

    # ---------------------------------------------------------
    # CASO 2: SINGULAR (Marca Error - Fila duplicada)
    # ---------------------------------------------------------
    A_error = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_error = [random.uniform(-10, 10) for _ in range(n)]
    
    # Truco: La segunda fila es exactamente el doble de la primera
    A_error[1] = [2 * x for x in A_error[0]]
    b_error[1] = 2 * b_error[0]
    guardar_matriz(A_error, b_error, "matriz_error.txt")

    # ---------------------------------------------------------
    # CASO 3: DESACOMODADA (Obliga a hacer pivoteo)
    # ---------------------------------------------------------
    A_des = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_des = [random.uniform(-10, 10) for _ in range(n)]
    
    # Truco: Llenamos la diagonal principal de ceros puros
    for i in range(n):
        A_des[i][i] = 0.0
    guardar_matriz(A_des, b_des, "matriz_desacomodada.txt")

    print("\n¡Listo! Tienes 3 archivos nuevos en tu carpeta listos para probar.")

if __name__ == "__main__":
    # Generamos matrices de 100x100
    generar_casos_prueba(1000)