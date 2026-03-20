
# Tema 3: Sistemas de Ecuaciones Lineales

Este módulo se enfoca en resolver sistemas de la forma $Ax = B$. El objetivo es encontrar el vector de incógnitas $x$ mediante procedimientos que transforman la matriz de coeficientes o se aproximan numéricamente a la solución.

---

## 1. Métodos Directos

Buscan transformar la matriz para obtener una solución exacta en un número finito de pasos.

### A. Eliminación Gaussiana
**Explicación:** Sistematiza la eliminación de incógnitas para transformar la matriz aumentada en una estructura triangular superior. Posteriormente, se utiliza la sustitución hacia atrás para hallar los valores de las variables.

**Algoritmo:**
1. **Construcción de la matriz aumentada:** Combinar coeficientes $A$ y resultados $B$.
2. **Pivoteo Parcial:** Intercambiar filas para colocar el elemento de mayor valor absoluto en la diagonal, evitando divisiones por cero y errores de redondeo.
3. **Eliminación hacia adelante:** Generar ceros debajo de la diagonal usando el factor:
   $$m_{ik} = \frac{a_{ik}}{a_{kk}}$$
4. **Sustitución hacia atrás:** Despejar las incógnitas desde la última ($x_n$) hasta la primera ($x_1$) usando:
   $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$$

**Pseudocódigo:**
```text
Función EliminaciónGaussiana(A, b):
    n = longitud(b)
    Para i de 0 a n-1:
        Pivoteo parcial (Intercambio de filas)
        Para j de i+1 a n-1:
            factor = A[j][i] / A[i][i]
            Actualizar fila j: A[j] = A[j] - factor * A[i]
    
    // Sustitución
    Para i de n-1 a 0:
        suma = Suma(A[i][j] * x[j] para j de i+1 a n-1)
        x[i] = (b[i] - suma) / A[i][i]
    Retornar x
Fin Función
```

### B. Gauss-Jordan
**Explicación:** Es una extensión de la eliminación gaussiana. En lugar de solo generar una matriz triangular superior, se eliminan los elementos tanto por encima como por debajo de la diagonal, convirtiendo la matriz de coeficientes en una **matriz identidad**.

**Algoritmo:**
1. Normalizar la fila del pivote dividiéndola entre el elemento diagonal $a_{ii}$.
2. Eliminar los elementos de la columna actual en todas las demás filas (arriba y abajo).
3. Repetir para cada columna hasta obtener la identidad en la parte izquierda de la matriz aumentada.
4. El vector resultante en la derecha es directamente la solución del sistema.

**Pseudocódigo:**
```text
Función GaussJordan(A, b):
    n = longitud(b)
    Para i de 0 a n-1:
        Normalizar fila i: A[i] = A[i] / A[i][i]
        Para j de 0 a n-1:
            Si i != j:
                factor = A[j][i]
                A[j] = A[j] - factor * A[i]
    Retornar b (columna de resultados transformada)
Fin Función
```

### C. Descomposición LU
**Explicación:** Factoriza la matriz $A$ en el producto de dos matrices: una triangular inferior ($L$) y una triangular superior ($U$), tal que $A = LU$. Es especialmente útil cuando se deben resolver múltiples sistemas con la misma matriz $A$ pero diferentes vectores $B$.

**Algoritmo:**
1. Descomponer la matriz $A$ en las matrices $L$ (con unos en la diagonal) y $U$ (obtenida mediante eliminación gaussiana).
2. Resolver el sistema intermedio $Ly = B$ mediante **sustitución hacia adelante**.
3. Resolver el sistema final $Ux = y$ mediante **sustitución hacia atrás**.

**Pseudocódigo:**
```text
Función DescomposiciónLU(A, b):
    L, U = Factorizar(A) // A = LU
    y = SustituciónHaciaAdelante(L, b) // Ly = b
    x = SustituciónHaciaAtrás(U, y)    // Ux = y
    Retornar x
Fin Función
```

---

## 2. Métodos Iterativos

Parten de una suposición inicial y refinan el resultado mediante ciclos hasta que el error es aceptable.

### A. Método de Jacobi
**Explicación:** Se despeja cada variable de la diagonal principal. En cada iteración, se utilizan únicamente los valores de la iteración anterior para calcular todos los nuevos valores de forma simultánea.

**Algoritmo:**
1. Verificar la dominancia diagonal de la matriz para asegurar convergencia.
2. Despejar cada variable $x_i$ de la ecuación correspondiente.
3. Sustituir los valores actuales en las fórmulas para obtener los valores de la siguiente iteración.
4. Repetir hasta que el error relativo porcentual sea menor a la tolerancia.

**Pseudocódigo:**
```text
Función Jacobi(A, b, tol, max_iter):
    x = vector_ceros(n)
    Repetir max_iter veces:
        x_nuevo = copiar(x)
        Para i de 0 a n-1:
            suma = Suma(A[i][j] * x[j] para j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        Si Error(x_nuevo, x) < tol: Retornar x_nuevo
        x = x_nuevo
Fin Función
```

### B. Método de Gauss-Seidel
**Explicación:** Es una optimización del método de Jacobi. En lugar de esperar a la siguiente iteración, utiliza los valores recién calculados de las variables de manera inmediata dentro del mismo ciclo, acelerando la convergencia.

**Algoritmo:**
1. Reordenar la matriz para buscar dominancia diagonal.
2. Establecer un vector inicial (generalmente ceros).
3. Calcular cada variable usando los valores más recientes disponibles:
   $$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}$$
4. Evaluar el error después de cada iteración completa hasta que sea menor a la tolerancia (ej. $1e-6$).

**Pseudocódigo:**
```text
Función GaussSeidel(A, b, tol, max_iter):
    x = vector_ceros(n)
    Para k de 1 a max_iter:
        x_viejo = copiar(x)
        Para i de 0 a n-1:
            suma = Suma(A[i][j] * x[j] para j != i) // Usa x[j] actualizados
            x[i] = (b[i] - suma) / A[i][i]
        Si abs(x - x_viejo) < tol: Retornar x
Fin Función
```
```

---

