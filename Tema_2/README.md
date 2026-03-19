# Tema 2: Algoritmos para la Aproximación de Raíces

Este apartado detalla los fundamentos teóricos y las fórmulas aplicadas para resolver ecuaciones no lineales de la forma $f(x) = 0$. El objetivo es encontrar el valor de $x$ que anula la función, una operación crítica para simulaciones y optimización en ingeniería.

## 1. Métodos Cerrados (o de Intervalo)

[cite_start]Estos métodos requieren de un intervalo inicial $[a, b]$ donde se sospecha que se encuentra la raíz[cite: 2]. [cite_start]Se basan en el **Teorema de Bolzano**, el cual dicta que si una función continua cambia de signo en los extremos del intervalo, existe al menos una raíz real en ese espacio[cite:2].

### A. Método de Bisección
Es el algoritmo más elemental y seguro. [cite_start]Consiste en dividir el intervalo a la mitad repetidamente hasta reducir el error a un nivel aceptable[cite:2].

**Algoritmo:**
1. Elegir valores iniciales $a$ y $b$ que encierren la raíz ($f(a) \cdot f(b) < 0$).
2. Calcular el punto medio $x_r$.
3. Determinar el subintervalo de búsqueda:
   - Si $f(a) \cdot f(x_r) < 0$, la raíz está a la izquierda; el nuevo $b = x_r$.
   - Si $f(a) \cdot f(x_r) > 0$, la raíz está a la derecha; el nuevo $a = x_r$.
4. Repetir hasta alcanzar la tolerancia deseada.

**Pseudocódigo:**
```text
Función Bisección(a, b, tol):
    Mientras ((b - a) / 2) > tol:
        xr = (a + b) / 2
        Si f(a) * f(xr) < 0:
            b = xr
        Sino:
            a = xr
    Retornar xr
Fin Función 
```

**Fórmula del punto medio:**
$$x_r = \frac{a + b}{2}$$

* [cite_start]**Criterio de decisión:** Si $f(a) \cdot f(x_r) < 0$, la raíz está en el subintervalo izquierdo; de lo contrario, está en el derecho[cite:2].

### B. Método de Falsa Posición 
A diferencia de la bisección, este método une los puntos $f(a)$ y $f(b)$ con una línea recta. [cite_start]La intersección de esta línea con el eje $x$ suele estar más cerca de la raíz real[cite:2].

**Fórmula de aproximación:**
$$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$



---

## 2. Métodos Abiertos

[cite_start]Estos algoritmos no requieren "encerrar" la raíz en un intervalo; utilizan uno o dos valores iniciales y fórmulas iterativas para proyectar la solución[cite: 2]. [cite_start]Aunque son mucho más rápidos, presentan el riesgo de **diverger** (alejarse de la solución) si el punto inicial es inadecuado o la función es muy irregular[cite: 2].

### A. Método de Newton-Raphson
[cite_start]Es uno de los métodos más eficientes debido a que utiliza la derivada de la función para encontrar la raíz mediante tangentes[cite: 2].

**Fórmula iterativa:**
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$

### B. Método de la Secante
Se utiliza cuando calcular la derivada de la función es difícil o costoso computacionalmente. [cite_start]Sustituye la derivada por una aproximación basada en dos puntos previos[cite:2].





---

## Diferencias Técnicas

| Característica | Métodos Cerrados | Métodos Abiertos |
| :--- | :--- | :--- |
| **Puntos iniciales** | [cite_start]Requieren un intervalo $[a, b]$[cite:2]. | [cite_start]Uno o dos puntos (no rodean la raíz)[cite:2]. |
| **Convergencia** | [cite_start]Siempre convergen si hay una raíz[cite:2]. | [cite_start]Pueden fallar (divergencia)[cite:2]. |
| **Velocidad** | [cite_start]Lenta (lineal)[cite:2]. | [cite_start]Muy rápida (cuadrática en Newton)[cite:2]. |
| **Estabilidad** | [cite_start]Alta[cite:2]. | [cite_start]Depende del valor inicial[cite:2]. |



---
[Volver al menu principal](../README.md)