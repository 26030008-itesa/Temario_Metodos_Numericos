
# Tema 3: Sistemas de Ecuaciones Lineales

[cite_start]Este módulo se enfoca en resolver sistemas de la forma $Ax = B$, donde se busca encontrar los valores de un vector de incógnitas $x$ que satisfagan múltiples ecuaciones simultáneamente[cite: 1]. [cite_start]Los métodos se dividen en directos (soluciones exactas) e iterativos (aproximaciones sucesivas)[cite: 1].

---

## 1. Métodos Directos

[cite_start]Estos métodos transforman la matriz original mediante operaciones algebraicas para despejar las variables de forma sistemática[cite: 1].

### A. Eliminación Gaussiana
[cite_start]**Explicación:** Sistematiza el proceso de eliminación de incógnitas para transformar la matriz aumentada en una estructura triangular superior[cite: 1]. [cite_start]Una vez obtenida esta forma, las variables se despejan mediante sustitución hacia atrás, comenzando desde la última incógnita hasta la primera[cite: 1].



[cite_start]**Algoritmo:** 1. **Construcción de la matriz aumentada:** Integrar los coeficientes $A$ y los resultados $B$ en una sola estructura[cite: 1].
2. [cite_start]**Pivoteo Parcial:** En cada columna, buscar el elemento con el valor absoluto máximo para intercambiar filas, lo que minimiza errores de redondeo y evita divisiones por cero[cite: 1].
3. [cite_start]**Eliminación hacia adelante:** Generar ceros por debajo de la diagonal principal usando un factor multiplicador[cite: 1].
   - [cite_start]**Fórmula del factor:** $m_{ik} = \frac{a_{ik}}{a_{kk}}$ [cite: 1]
4. [cite_start]**Sustitución hacia atrás:** Despejar las variables desde $x_n$ hasta $x_1$[cite: 1].
   - [cite_start]**Fórmula de sustitución:** $x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$ [cite: 1]

**Pseudocódigo:** ```text
Función EliminaciónGaussiana(A, b):
    n = longitud(b)
    // Fase de eliminación
    Para i desde 0 hasta n-1:
        Pivoteo parcial (Intercambiar filas si es necesario)
        Para j desde i+1 hasta n:
            factor = M[j][i] / M[i][i]
            Actualizar fila M[j] = M[j] - factor * M[i]
    
    // Fase de sustitución
    Para i desde n-1 hasta 0:
        suma = Suma(M[i][j] * x[j] para j desde i+1 hasta n)
        x[i] = (M[i][n] - suma) / M[i][i]
    Retornar x
Fin Función
```

---

## 2. Métodos Iterativos

[cite_start]A diferencia de los directos, estos métodos parten de una suposición inicial y mejoran la aproximación en cada ciclo hasta alcanzar una tolerancia de error predefinida[cite: 1].

### A. Método de Gauss-Seidel
[cite_start]**Explicación:** Es un procedimiento que busca la solución mediante aproximaciones sucesivas[cite: 1]. [cite_start]Su característica principal es que utiliza los valores recién calculados de las variables dentro de la misma iteración para hallar las siguientes, lo que acelera la convergencia en comparación con otros métodos como Jacobi[cite: 1].



[cite_start]**Algoritmo:** 1. **Reordenamiento Diagonal:** Organizar la matriz para que los elementos de la diagonal principal sean mayores a la suma de los demás elementos de su fila (Dominancia Diagonal)[cite: 1].
2. [cite_start]**Suposición Inicial:** Establecer un vector de inicio, comúnmente un vector de ceros $[0, 0, 0]$[cite: 1].
3. [cite_start]**Proceso Iterativo:** Calcular el nuevo valor de cada variable usando la fórmula de actualización[cite: 1].
   - [cite_start]**Fórmula:** $x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}$ [cite: 1]
4. [cite_start]**Criterio de Convergencia:** Detener el proceso cuando la diferencia entre la iteración actual y la anterior sea menor a la tolerancia (ej. $1e-6$)[cite: 1].

**Pseudocódigo:** ```text
Función GaussSeidel(A, b, tol, max_iter):
    x = vector_de_ceros(n)
    Para k desde 0 hasta max_iter:
        error_maximo = 0
        Para i desde 0 hasta n:
            x_viejo = x[i]
            suma = Suma(A[i][j] * x[j] para j != i)
            x[i] = (b[i] - suma) / A[i][i]
            error_actual = abs(x[i] - x_viejo)
            Si error_actual > error_maximo: error_maximo = error_actual
        
        Si error_maximo < tol: Retornar x (Éxito)
    Retornar Error (No convergió)
Fin Función
```

---

## Diferencias Técnicas y Análisis

[cite_start]En sistemas de ecuaciones reales, la elección del método es fundamental[cite: 1]:

* [cite_start]**Sensibilidad:** La Eliminación Gaussiana es más sensible a la arquitectura del sistema; si hay dependencia lineal (matriz singular), el método se detiene para evitar errores[cite: 1].
* [cite_start]**Resiliencia:** Gauss-Seidel puede mostrar mayor resistencia en sistemas grandes si se aplica un reordenamiento diagonal previo, aunque requiere supervisión constante de la tolerancia de error[cite: 1].

| Característica | Métodos Directos | Métodos Iterativos |
| :--- | :--- | :--- |
| **Tipo de resultado** | [cite_start]Exacto (teórico)[cite: 1]. | [cite_start]Aproximación sucesiva[cite: 1]. |
| **Uso de memoria** | [cite_start]Alto en matrices grandes[cite: 1]. | [cite_start]Eficiente en sistemas masivos[cite: 1]. |
| **Diagnóstico** | [cite_start]Detecta matrices singulares[cite: 1]. | [cite_start]Requiere dominancia diagonal[cite: 1]. |

