# Tema 5: Interpolación y Ajuste de Funciones

Este módulo abarca los métodos para estimar valores entre datos conocidos (interpolación) y para encontrar la función que mejor describe un conjunto de datos con ruido (ajuste o regresión).

---

## 1. Polinomio de Interpolación de Newton — `Newton/`

Construye el polinomio usando **diferencias divididas**, lo que permite agregar nuevos puntos de forma eficiente sin recalcular todo.

**Diferencias divididas:**
$$f[x_i, x_{i+1}, \ldots, x_{i+k}] = \frac{f[x_{i+1},\ldots,x_{i+k}] - f[x_i,\ldots,x_{i+k-1}]}{x_{i+k} - x_i}$$

**Polinomio:**
$$P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots$$

**Pseudocódigo:**
```text
ALGORITMO Newton
    ENTRADA: x[], y[], x_eval
    coef = DiferenciasDivididas(x, y)   // Vector de coeficientes
    resultado = coef[n-1]
    PARA i DESDE n-2 HASTA 0:
        resultado = resultado * (x_eval - x[i]) + coef[i]
    DEVOLVER resultado
FIN ALGORITMO
```

**Ventaja:** Agregar un punto nuevo solo añade un término al polinomio.

---

## 2. Polinomio de Interpolación de Lagrange — `Lagrange/`

Construye directamente el polinomio como combinación lineal de polinomios base $L_i(x)$.

$$P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x), \qquad L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$$

**Pseudocódigo:**
```text
ALGORITMO Lagrange
    ENTRADA: x[], y[], x_eval
    resultado = 0
    PARA i DESDE 0 HASTA n:
        L_i = 1
        PARA j DESDE 0 HASTA n:
            SI j != i: L_i *= (x_eval - x[j]) / (x[i] - x[j])
        resultado += y[i] * L_i
    DEVOLVER resultado
FIN ALGORITMO
```

**Ventaja:** Formulación directa y simétrica; no requiere tabla auxiliar.

---

## 3. Interpolación Segmentada (Splines Cúbicos) — `Interpolacion_Segmentada/`

En lugar de un único polinomio de grado alto (que produce el **fenómeno de Runge**), se ajusta un polinomio cúbico a cada par de puntos consecutivos, garantizando continuidad de la función y sus primeras dos derivadas.

**En cada segmento $[x_i, x_{i+1}]$:**
$$S_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3$$

**Condiciones (Spline Natural):** $S''(x_0) = S''(x_n) = 0$

**Pseudocódigo:**
```text
ALGORITMO SplineCubicoNatural
    ENTRADA: x[], y[]
    h[i] = x[i+1] - x[i]
    Construir sistema tridiagonal para c[i]  // Momentos
    Resolver con Algoritmo de Thomas
    Calcular b[i] y d[i] desde c[i]
    DEVOLVER a[], b[], c[], d[]
FIN ALGORITMO
```

---

## 4. Regresión y Mínimos Cuadrados — `Minimos_Cuadrados/`

Cuando los datos tienen ruido experimental, la interpolación exacta no es conveniente. En cambio, se minimiza la suma de los cuadrados de los residuos:

$$\min \sum_{i=0}^{n} \left[y_i - P(x_i)\right]^2$$

Para un polinomio de grado $m$, esto lleva al **sistema normal:**
$$A^T A\, \mathbf{c} = A^T \mathbf{y}$$

donde $A$ es la matriz de Vandermonde.

**Pseudocódigo:**
```text
ALGORITMO MinimosCuadrados
    ENTRADA: x[], y[], grado m
    A = Vandermonde(x, m)          // Matriz n × (m+1)
    Calcular AtA = A^T * A
    Calcular Aty = A^T * y
    c = EliminaciónGaussiana(AtA, Aty)
    DEVOLVER c
FIN ALGORITMO
```

**Bondad del ajuste:** Coeficiente de determinación $R^2 \in [0, 1]$ — más cercano a 1 indica mejor ajuste.

---

## Comparativa de Métodos

| Método | Pasa por todos los puntos | Grado máximo | Mejor para |
|--------|:-------------------------:|:------------:|------------|
| Newton / Lagrange | ✅ | $n$ | Datos exactos, sin ruido |
| Spline Cúbico | ✅ | 3 por segmento | Suavidad, evitar Runge |
| Mínimos Cuadrados | ❌ (ajuste) | Elegido | Datos experimentales con ruido |

---

## Notas de Implementación

- El **fenómeno de Runge** (oscilaciones en los extremos) ocurre con polinomios de alto grado y puntos igualmente espaciados; los Splines lo evitan.
- Para **mínimos cuadrados**, el sistema normal $A^T A$ puede ser mal condicionado con grados altos; se recomienda no exceder grado 5-6 en la práctica.
- Newton es preferido sobre Lagrange cuando los datos llegan de forma incremental.
