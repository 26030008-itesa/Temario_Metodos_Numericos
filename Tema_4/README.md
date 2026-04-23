Claro que sí. He generado el archivo README.md siguiendo rigurosamente las especificaciones de estructura, estilo técnico y notación solicitadas para tu repositorio.

# Tema X: Métodos de Integración Numérica

Este repositorio contiene la fundamentación teórica, algoritmos y pseudocódigos de los métodos más utilizados en el análisis numérico para la aproximación de derivadas e integrales definidas. Estos métodos son esenciales cuando se trabaja con funciones cuya antiderivada es desconocida o cuando se dispone únicamente de un conjunto discreto de datos experimentales.

---

## 1. Métodos de Diferenciación Numérica

La diferenciación numérica aproxima la tasa de cambio de una función utilizando valores discretos en puntos cercanos. La precisión de estas aproximaciones depende del número de nodos utilizados y del tamaño del paso $h$.[1, 2]

### A. Regla de 3 puntos
La regla de tres puntos utiliza expansiones de Taylor para obtener fórmulas de segundo orden $O(h^2)$. Dependiendo de la posición del punto de interés $x_0$ respecto a los nodos disponibles, se aplican tres variantes.[2, 3]

**Fórmulas matemáticas:**

*   **Diferencia Central (más precisa):**
    $$f'(x_0) = \frac{f(x_0 + h) - f(x_0 - h)}{2h}$$
*   **Diferencia Hacia Adelante (Forward):**
    $$f'(x_0) = \frac{-3f(x_0) + 4f(x_0 + h) - f(x_0 + 2h)}{2h}$$
*   **Diferencia Hacia Atrás (Backward):**
    $$f'(x_0) = \frac{3f(x_0) - 4f(x_0 - h) + f(x_0 - 2h)}{2h}$$

**Algoritmo paso a paso:**
1.  Definir el punto de evaluación $x_0$ y el tamaño del paso $h$.
2.  Identificar la disponibilidad de puntos: si existen datos a ambos lados, usar la fórmula central; de lo contrario, usar las fórmulas laterales.[2, 4]
3.  Evaluar la función $f(x)$ en los nodos requeridos ($x_0, x_0 \pm h, x_0 \pm 2h$).
4.  Sustituir los valores en la fórmula correspondiente para obtener la aproximación de la derivada.

**Pseudocódigo:**
ALGORITMO Diferenciacion3Puntos
    ENTRADA: f (funcion), x0 (punto), h (paso), tipo (1:Adelante, 2:Atras, 3:Central)
    
    SI tipo == 1 ENTONCES
        derivada = (-3*f(x0) + 4*f(x0 + h) - f(x0 + 2*h)) / (2 * h)
    SINO SI tipo == 2 ENTONCES
        derivada = (3*f(x0) - 4*f(x0 - h) + f(x0 - 2*h)) / (2 * h)
    SINO SI tipo == 3 ENTONCES
        derivada = (f(x0 + h) - f(x0 - h)) / (2 * h)
    
    DEVOLVER derivada
FIN ALGORITMO

### B. Regla de 5 puntos
Estas fórmulas ofrecen una precisión de cuarto orden $O(h^4)$, reduciendo significativamente el error de truncamiento. Son ideales para aplicaciones que requieren alta exactitud, aunque son más sensibles al error de redondeo si $h$ es extremadamente pequeño.[5, 6]

**Fórmulas matemáticas:**

*   **Diferencia Central (Punto medio):**
    $$f'(x_0) = \frac{f(x_0 - 2h) - 8f(x_0 - h) + 8f(x_0 + h) - f(x_0 + 2h)}{12h}$$
*   **Diferencia Hacia Adelante:**
    $$f'(x_0) = \frac{-25f(x_0) + 48f(x_0 + h) - 36f(x_0 + 2h) + 16f(x_0 + 3h) - 3f(x_0 + 4h)}{12h}$$

**Algoritmo:**
1.  Establecer $x_0$ y un valor de $h$ que optimice el compromiso entre truncamiento y redondeo.[1, 7]
2.  Obtener las 5 evaluaciones de la función según el esquema elegido (central o lateral).
3.  Aplicar los coeficientes específicos (ej. 1, -8, 8, -1 para el esquema central) dividiendo por $12h$.

**Pseudocódigo:**
ALGORITMO Diferenciacion5PuntosCentral
    ENTRADA: f, x0, h
    P1 = f(x0 - 2*h)
    P2 = f(x0 - h)
    P3 = f(x0 + h)
    P4 = f(x0 + 2*h)
    
    resultado = (P1 - 8*P2 + 8*P3 - P4) / (12 * h)
    DEVOLVER resultado
FIN ALGORITMO

---

## 2. Métodos de Integración Numérica

La integración numérica (cuadratura) sustituye el integrando por un polinomio interpolador que se integra fácilmente sobre el intervalo $[a, b]$.[8, 4]

### A. Método del Trapecio
Aproxima el área bajo la curva mediante segmentos lineales, formando trapecios. Es el método más simple de las fórmulas de Newton-Cotes.[1, 9]

**Fórmulas:**
*   **Simple:** $I \approx \frac{h}{2} [f(a) + f(b)]$
*   **Compuesta:** 
    $$\int_a^b f(x) dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$
    donde $h = \frac{b - a}{n}$.[5, 10]

**Algoritmo:**
1.  Definir límites $a, b$ y el número de subintervalos $n$.
2.  Calcular el ancho del intervalo $h$.
3.  Sumar los valores de la función en los extremos.
4.  Sumar el doble de los valores de la función en los puntos interiores $x_i = a + ih$.[11, 12]
5.  Multiplicar el total por $h/2$.

**Pseudocódigo:**
ALGORITMO TrapecioCompuesto
    ENTRADA: f, a, b, n
    h = (b - a) / n
    suma = f(a) + f(b)
    
    PARA i DESDE 1 HASTA n-1
        x = a + i * h
        suma = suma + 2 * f(x)
    FIN PARA
    
    DEVOLVER suma * (h / 2)
FIN ALGORITMO

### B. Método de Simpson 1/3
Aproxima la función mediante polinomios de segundo grado (parábolas). Proporciona una precisión de tercer grado $O(h^4)$.[8, 13]

**Restricción crítica:** El número de subintervalos $n$ debe ser obligatoriamente **par**.[14, 15]

**Fórmula Compuesta:**
$$\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1,3,5}^{n-1} f(x_i) + 2 \sum_{j=2,4,6}^{n-2} f(x_j) + f(x_n) \right]$$

**Algoritmo:**
1.  Validar que $n$ sea par.
2.  Calcular $h = (b-a)/n$.
3.  Evaluar la función en los extremos $x_0, x_n$.
4.  Multiplicar por 4 los nodos de índice impar y por 2 los nodos de índice par interiores.[9, 16]
5.  Multiplicar la suma total por $h/3$.

**Pseudocódigo:**
ALGORITMO Simpson1tercio
    ENTRADA: f, a, b, n (donde n es par)
    h = (b - a) / n
    suma = f(a) + f(b)
    
    PARA i DESDE 1 HASTA n-1
        x = a + i * h
        SI i MOD 2!= 0 ENTONCES
            suma = suma + 4 * f(x)
        SINO
            suma = suma + 2 * f(x)
        FIN SI
    FIN PARA
    
    DEVOLVER suma * (h / 3)
FIN ALGORITMO

### C. Método de Simpson 3/8
Utiliza polinomios de tercer grado para la interpolación. Posee el mismo orden de error que Simpson 1/3 pero es útil para configuraciones de datos específicas.[8, 17]

**Restricción crítica:** El número de subintervalos $n$ debe ser **múltiplo de 3**.[18, 16]

**Fórmula Compuesta:**
$$\int_a^b f(x) dx \approx \frac{3h}{8} \left[ f(x_0) + 3 \sum_{i \neq 3,6,9 \dots} f(x_i) + 2 \sum_{j=3,6,9 \dots}^{n-3} f(x_j) + f(x_n) \right]$$
*Nota: Los coeficientes internos siguen el patrón 3, 3, 2, 3, 3, 2...*

**Algoritmo:**
1.  Verificar que $n \pmod 3 == 0$.
2.  Calcular $h = (b-a)/n$.
3.  Asignar pesos a los nodos: el primero y último tienen peso 1, los múltiplos de 3 tienen peso 2, y los demás tienen peso 3.
4.  Multiplicar la suma por $3h/8$.

**Pseudocódigo:**
ALGORITMO Simpson3octavos
    ENTRADA: f, a, b, n (donde n es multiplo de 3)
    h = (b - a) / n
    suma = f(a) + f(b)
    
    PARA i DESDE 1 HASTA n-1
        x = a + i * h
        SI i MOD 3 == 0 ENTONCES
            suma = suma + 2 * f(x)
        SINO
            suma = suma + 3 * f(x)
        FIN SI
    FIN PARA
    
    DEVOLVER suma * (3 * h / 8)
FIN ALGORITMO

---

## Notas de Implementación
*   **Precisión:** Simpson 1/3 es generalmente preferido sobre Trapecio por su mayor orden de error, siempre que se cumpla la paridad de $n$.[15]
*   **Combinación de Métodos:** Si un conjunto de datos tiene un número impar de intervalos que no es múltiplo de 3, se puede aplicar Simpson 1/3 en los primeros $n-3$ intervalos y Simpson 3/8 en los últimos 3 para mantener la precisión $O(h^4)$.[19, 15]
*   **Estabilidad:** En diferenciación, reducir $h$ demasiado puede causar errores catastróficos por resta de números casi iguales (redondeo).

Espero que este documento te sea de gran utilidad para tu proyecto en GitHub. ¡Mucho éxito con tu problemario!