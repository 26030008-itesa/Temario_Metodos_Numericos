import random

def guardar_matriz(matriz, vector, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for i in range(len(matriz)):
            fila_completa = matriz[i] + [vector[i]]
            linea_texto = " ".join([f"{num:10.6f}" for num in fila_completa])
            archivo.write(linea_texto + "\n")
    print(f"[*] Archivo creado exitosamente: {nombre_archivo}")

def generar_casos_prueba(n):
    print(f"Generando los 5 casos de prueba para sistemas de {n}x{n}...\n")

    # CASO 1: NORMAL
    A_normal = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_normal = [random.uniform(-10, 10) for _ in range(n)]
    guardar_matriz(A_normal, b_normal, "matriz_normal.txt")

    # CASO 2: SINGULAR (Error)
    A_error = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_error = [random.uniform(-10, 10) for _ in range(n)]
    A_error[1] = [2 * x for x in A_error[0]]
    b_error[1] = 2 * b_error[0]
    guardar_matriz(A_error, b_error, "matriz_error.txt")

    # CASO 3: DESACOMODADA NORMAL (Puros ceros en diagonal)
    A_des = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_des = [random.uniform(-10, 10) for _ in range(n)]
    for i in range(n):
        A_des[i][i] = 0.0
    guardar_matriz(A_des, b_des, "matriz_desacomodada.txt")

    # CASO 4: PERFECTAMENTE DOMINANTE
    A_dom = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_dom = [random.uniform(-10, 10) for _ in range(n)]
    for i in range(n):
        suma_sin_diagonal = sum(abs(x) for x in A_dom[i]) - abs(A_dom[i][i])
        A_dom[i][i] = suma_sin_diagonal + random.uniform(1.0, 50.0)
        if random.choice([True, False]):
            A_dom[i][i] *= -1
    guardar_matriz(A_dom, b_dom, "matriz_dominante.txt")

    # ---------------------------------------------------------
    # CASO 5: DOMINANTE PERO DESORDENADA (¡El Jefe Final!)
    # ---------------------------------------------------------
    # 1. Copiamos exactamente la lógica del caso 4 para hacerla dominante
    A_oculta = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
    b_oculta = [random.uniform(-10, 10) for _ in range(n)]
    for i in range(n):
        suma_sin_diagonal = sum(abs(x) for x in A_oculta[i]) - abs(A_oculta[i][i])
        A_oculta[i][i] = suma_sin_diagonal + random.uniform(1.0, 50.0)
        if random.choice([True, False]):
            A_oculta[i][i] *= -1

    # 2. Unimos temporalmente la matriz y el vector para no perder la relación al mezclar
    filas_completas = []
    for i in range(n):
        filas_completas.append(A_oculta[i] + [b_oculta[i]])
        
    # 3. ¡Mezclamos todas las filas al azar! Esto destruye la diagonal visualmente.
    random.shuffle(filas_completas)
    
    # 4. Volvemos a separar los coeficientes y los resultados
    A_desordenada = [fila[:-1] for fila in filas_completas]
    b_desordenada = [fila[-1] for fila in filas_completas]
    
    guardar_matriz(A_desordenada, b_desordenada, "matriz_dominante_desordenada.txt")

    print("\n¡Listo! Tienes 5 archivos nuevos en tu carpeta listos para probar.")

if __name__ == "__main__":
    generar_casos_prueba(1000)