¡Claro! He limpiado las etiquetas de citación y optimizado el formato para que se vea impecable en GitHub, utilizando bloques de código con resaltado de sintaxis y ecuaciones en LaTeX.

Aquí tienes el código Markdown listo para copiar:

---

```markdown
# Tema 2: Algoritmos para la Aproximación de Raíces

En el análisis numérico, encontrar la raíz de una función $f(x) = 0$ consiste en determinar el valor de la variable independiente que anula la función. Para un ingeniero, esto es esencial para resolver problemas donde no existe una solución analítica directa.

---

## 1. Métodos Cerrados (o de Intervalo)

Estos métodos requieren de un intervalo inicial $[a, b]$ que "encierre" la raíz. Son robustos y siempre convergen si la función es continua y existe un cambio de signo en los extremos ($f(a) \cdot f(b) < 0$), de acuerdo con el **Teorema de Bolzano**.

### A. Método de Bisección
**¿Qué es?** Es el método más elemental y consiste en dividir repetidamente el intervalo a la mitad hasta que el segmento restante sea lo suficientemente pequeño para cumplir con la tolerancia deseada.

**Algoritmo:**
1. Identificar un intervalo $[a, b]$ donde haya un cambio de signo.
2. Calcular el punto medio $x_r = \frac{a + b}{2}$.
3. Evaluar la función en el punto medio:
    * Si $f(a) \cdot f(x_r) < 0$, la raíz está en la mitad izquierda; actualizar $b = x_r$.
    * Si $f(a) \cdot f(x_r) > 0$, la raíz está en la mitad derecha; actualizar $a = x_r$.
4. Repetir el proceso hasta que el error relativo sea menor a la tolerancia.

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

### B. Método de Falsa Posición (Regula Falsi)
**¿Qué es?** A diferencia de la bisección, este método aprovecha una visualización geométrica uniendo $f(a)$ y $f(b)$ con una línea recta. El punto donde esta línea cruza el eje $x$ suele ser una aproximación más rápida a la raíz real.

**Algoritmo:**
1. Definir el intervalo $[a, b]$ con cambio de signo.
2. Calcular la aproximación $x_r$ usando la intersección de la secante:
   $$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$
3. Verificar el signo de $f(a) \cdot f(x_r)$ para redefinir los límites del intervalo.
4. Iterar hasta que el valor de la función en $x_r$ sea cercano a cero o se alcance la tolerancia.

**Pseudocódigo:**
```text
Función FalsaPosicion(a, b, tol):
    Repetir:
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        Si f(a) * f(xr) < 0:
            b = xr
        Sino:
            a = xr
    Hasta que abs(f(xr)) < tol
    Retornar xr
Fin Función
```

---

## 2. Métodos Abiertos

A diferencia de los cerrados, estos no necesitan un intervalo que rodee la raíz. Utilizan puntos iniciales arbitrarios y suelen ser mucho más rápidos, aunque corren el riesgo de **diverger** (alejarse de la solución) si la función es compleja.

### A. Método de Newton-Raphson
**¿Qué es?** Es un método basado en el cálculo diferencial que utiliza la recta tangente a la curva en un punto dado para proyectar la siguiente aproximación hacia la raíz.

**Algoritmo:**
1. Elegir un valor inicial $x_i$.
2. Calcular la pendiente de la función mediante su derivada $f'(x_i)$.
3. Obtener el siguiente punto con la fórmula:
   $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
4. Repetir hasta que la diferencia entre iteraciones sea mínima.

**Pseudocódigo:**
```text
Función NewtonRaphson(xi, tol):
    Hacer:
        x_nuevo = xi - f(xi) / f_derivada(xi)
        error = abs(x_nuevo - xi)
        xi = x_nuevo
    Mientras error > tol
    Retornar xi
Fin Función
```

### B. Método de la Secante
**¿Qué es?** Es una variante de Newton-Raphson diseñada para casos donde la derivada de la función es difícil de calcular. En su lugar, utiliza dos puntos previos para estimar la pendiente.

**Algoritmo:**
1. Seleccionar dos valores iniciales $x_0$ y $x_1$.
2. Calcular la pendiente aproximada entre ambos puntos.
3. Encontrar la nueva aproximación $x_{i+1}$ mediante la fórmula iterativa:
   $$x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}$$
4. Actualizar los puntos ($x_{i-1} = x_i$ y $x_i = x_{i+1}$) y repetir.

**Pseudocódigo:**
```text
Función Secante(x0, x1, tol):
    Hacer:
        x_nuevo = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        error = abs(x_nuevo - x1)
        x0 = x1
        x1 = x_nuevo
    Mientras error > tol
    Retornar x1
Fin Función
```

### C. Iteración de Punto Fijo
**¿Qué es?** Consiste en transformar la ecuación $f(x) = 0$ en la forma $x = g(x)$. El método busca el punto donde la entrada y la salida de la función son iguales.

**Algoritmo:**
1. Despejar $x$ para encontrar la función $g(x)$.
2. Elegir una semilla o valor inicial $x_0$.
3. Calcular $x_{i+1} = g(x_i)$.
4. Iterar hasta que el valor se estabilice (el error sea menor a la tolerancia).

**Pseudocódigo:**
```text
Función PuntoFijo(x0, tol):
    Hacer:
        x_nuevo = g(x0)
        error = abs(x_nuevo - x0)
        x0 = x_nuevo
    Mientras error > tol
    Retornar x0
Fin Función
```
```

---

¿Te gustaría que agregue una tabla comparativa al final para resaltar las ventajas y desventajas de cada método? Sería un gran detalle para tu repositorio.