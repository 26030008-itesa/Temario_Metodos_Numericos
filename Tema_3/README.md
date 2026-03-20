
# Tema 3: Sistemas de Ecuaciones Lineales

Este módulo se enfoca en resolver sistemas de la forma $Ax = B$, donde se busca encontrar los valores de un vector de incógnitas $x$ que satisfagan múltiples ecuaciones simultáneamente. Los métodos se dividen en **directos** (soluciones exactas mediante álgebra) e **iterativos** (aproximaciones sucesivas hasta alcanzar una tolerancia).

---

## 1. Métodos Directos

Estos métodos transforman la matriz original mediante operaciones algebraicas para despejar las variables de forma sistemática.

### A. Eliminación Gaussiana
**Explicación:** Sistematiza el proceso de eliminación de incógnitas para transformar la matriz aumentada en una estructura triangular superior. Una vez obtenida esta forma, las variables se despejan mediante sustitución hacia atrás, comenzando desde la última incógnita hasta la primera.

**Algoritmo:**
1. **Construcción de la matriz aumentada:** Integrar los coeficientes $A$ y los resultados $B$ en una sola estructura.
2. **Pivoteo Parcial:** En cada columna, buscar el elemento con el valor absoluto máximo para intercambiar filas, lo que minimiza errores de redondeo y evita divisiones por cero.
3. **Eliminación hacia adelante:** Generar ceros por debajo de la diagonal principal usando un factor multiplicador.
   - **Fórmula del factor:** $$m_{ik} = \frac{a_{ik}}{a_{kk}}$$
4. **Sustitución hacia atrás:** Despejar las variables desde $x_n$ hasta $x_1$.
   - **Fórmula de sustitución:** $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$$

**Pseudocódigo:**
```text
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

A diferencia de los directos, estos métodos parten de una suposición inicial y mejoran la aproximación en cada ciclo hasta alcanzar una tolerancia de error predefinida.

### A. Método de Gauss-Seidel
**Explicación:** Es un procedimiento que busca la solución mediante aproximaciones sucesivas. Su característica principal es que utiliza los valores recién calculados de las variables dentro de la misma iteración para hallar las siguientes, lo que acelera la convergencia en comparación con otros métodos como Jacobi.

**Algoritmo:**
1. **Reordenamiento Diagonal:** Organizar la matriz para que sea **diagonalmente dominante** (los elementos de la diagonal principal deben ser mayores a la suma de los demás elementos de su fila).
2. **Suposición Inicial:** Establecer un vector de inicio, comúnmente un vector de ceros $[0, 0, 0]$.
3. **Proceso Iterativo:** Calcular el nuevo valor de cada variable usando la fórmula de actualización.

**Fórmula:**
$$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}$$

**Criterio de Convergencia:** Detener el proceso cuando la diferencia entre la iteración actual y la anterior sea menor a la tolerancia (ej. $1 \times 10^{-6}$).

**Pseudocódigo:**
```text
Función GaussSeidel(A, b, tol, max_iter):
    x = vector_de_ceros(n)
    Para k desde 0 hasta max_iter:
        error_maximo = 0
        Para i desde 0 hasta n:
            x_viejo = x[i]
            suma = Suma(A[i][j] * x[j] para j != i)
            x[i] = (b[i] - suma) / A[i][i]
            error_actual = abs(x[i] - x_viejo)
            Si error_actual > error_maximo: 
                error_maximo = error_actual
        
        Si error_maximo < tol: 
            Retornar x (Éxito)
            
    Retornar Error ("No convergió")
Fin Función
```

---

## Diferencias Técnicas y Análisis

En sistemas de ecuaciones reales, la elección del método es fundamental:

* **Sensibilidad:** La Eliminación Gaussiana es más sensible a la arquitectura del sistema; si hay dependencia lineal (matriz singular), el método se detiene para evitar errores catastróficos.
* **Resiliencia:** Gauss-Seidel puede mostrar mayor resistencia en sistemas grandes si se aplica un reordenamiento diagonal previo, aunque requiere supervisión constante de la tolerancia de error.

| Característica | Métodos Directos | Métodos Iterativos |
| :--- | :--- | :--- |
| **Tipo de resultado** | Exacto (teórico). | Aproximación sucesiva. |
| **Uso de memoria** | Alto en matrices grandes. | Eficiente en sistemas masivos. |
| **Diagnóstico** | Detecta matrices singulares. | Requiere dominancia diagonal. |

---
*Este material documenta los procedimientos validados en el examen de la unidad para la materia de Métodos Numéricos.*
```

---
