# Tema 3: Sistemas de Ecuaciones Lineales

Este módulo del proyecto aborda la resolución de sistemas de ecuaciones lineales simultáneas de la forma $Ax = B$. [cite_start]Se exploran tanto métodos directos (que buscan una solución exacta) como métodos iterativos (que se aproximan a la solución mediante ciclos)[cite: 1, 33].

## 1. Métodos Directos
[cite_start]Estos algoritmos transforman la matriz original en una estructura más simple para despejar las variables de forma sistemática[cite: 45].

### A. Eliminación Gaussiana
[cite_start]Es el método base que consiste en eliminar incógnitas mediante operaciones entre filas hasta obtener una matriz triangular superior[cite: 45]. El proceso incluye:
1. [cite_start]**Pivoteo Parcial:** Selección del elemento mayor en la columna para evitar divisiones por cero y reducir errores de redondeo[cite: 48].
2. [cite_start]**Eliminación hacia adelante:** Uso de un factor $m_{ik}$ para generar ceros debajo de la diagonal[cite: 49].
   $$m_{ik} = \frac{a_{ik}}{a_{kk}}$$
3. [cite_start]**Sustitución hacia atrás:** Despeje de variables desde la última hasta la primera[cite: 50].
   $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$$

### B. Gauss-Jordan
[cite_start]Una variante de la eliminación gaussiana donde se eliminan elementos tanto arriba como abajo de la diagonal principal, transformando la matriz de coeficientes directamente en una **matriz identidad**[cite: 1]. [cite_start]Esto permite que el vector de resultados sea directamente la solución sin necesidad de sustitución hacia atrás[cite: 1].

---

## 2. Métodos Iterativos
[cite_start]Se utilizan principalmente para sistemas grandes donde los métodos directos consumirían demasiada memoria o tiempo de procesamiento[cite: 56].

### A. Método de Jacobi
[cite_start]En este método, se despeja cada variable de la diagonal y se utilizan los valores de la iteración anterior para calcular todos los nuevos valores de forma simultánea[cite: 1].

**Fórmula iterativa:**
$$x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij}x_j^{(k)}}{a_{ii}}$$

### B. Método de Gauss-Seidel
Es una mejora del método de Jacobi. [cite_start]La diferencia principal es que, en cuanto se calcula el valor de una variable, ese valor "nuevo" se utiliza inmediatamente para calcular las variables restantes en la misma iteración, lo que acelera la convergencia[cite: 60].

**Fórmula iterativa:**
$$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij}x_j^{(k+1)} - \sum_{j > i} a_{ij}x_j^{(k)}}{a_{ii}}$$

---

## 3. Criterios de Convergencia y Error
[cite_start]Para asegurar que los métodos iterativos funcionen, es ideal que la matriz sea **Diagonalmente Dominante**, es decir, que el valor absoluto del elemento en la diagonal sea mayor a la suma de los demás elementos de su fila[cite: 58].

**Cálculo del Error Relativo Porcentual ($e_a$):**
[cite_start]En cada iteración, se mide la precisión del cálculo comparando el valor actual con el anterior[cite: 61]:
$$e_a = \left| \frac{x_i^{nuevo} - x_i^{anterior}}{x_i^{nuevo}} \right| \times 100\%$$

---

## Comparativa de Desempeño

| Característica | Métodos Directos | Métodos Iterativos |
| :--- | :--- | :--- |
| **Tipo de Solución** | [cite_start]Exacta (teóricamente)[cite: 1]. | [cite_start]Aproximada[cite: 56]. |
| **Uso de Memoria** | [cite_start]Alto en matrices grandes[cite: 1]. | [cite_start]Bajo y eficiente[cite: 1]. |
| **Matrices Especiales** | [cite_start]Sensibles a matrices singulares[cite: 82]. | [cite_start]Requieren dominancia diagonal[cite: 58]. |

---
[Volver al menu principal](../README.md)