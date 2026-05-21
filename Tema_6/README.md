# Tema 6: Solución de Ecuaciones Diferenciales

Este módulo cubre los métodos numéricos para resolver Problemas de Valor Inicial (PVI) de la forma:
$$y' = f(t, y), \quad y(t_0) = y_0$$

---

## 1. Métodos de Un Paso

### A. Método de Euler — `Euler/`

El método más simple: la derivada en el punto actual aproxima la pendiente en todo el paso.

$$y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

**Pseudocódigo:**
```text
ALGORITMO Euler
    ENTRADA: f, t0, y0, tf, h
    t = t0,  y = y0
    MIENTRAS t < tf:
        y = y + h * f(t, y)
        t = t + h
    DEVOLVER t, y
FIN ALGORITMO
```

**Orden de error:** $O(h)$ — al reducir $h$ a la mitad, el error global se reduce a la mitad.  
**Desventaja:** Acumula error rápidamente; solo útil con $h$ muy pequeño.

---

### B. Runge-Kutta de Orden 4 (RK4) — `Runge_Kutta/`

Combina 4 evaluaciones de $f$ por paso para lograr precisión de cuarto orden.

$$k_1 = h \cdot f(t_n, y_n)$$
$$k_2 = h \cdot f\!\left(t_n + \tfrac{h}{2},\; y_n + \tfrac{k_1}{2}\right)$$
$$k_3 = h \cdot f\!\left(t_n + \tfrac{h}{2},\; y_n + \tfrac{k_2}{2}\right)$$
$$k_4 = h \cdot f(t_n + h,\; y_n + k_3)$$
$$y_{n+1} = y_n + \frac{k_1 + 2k_2 + 2k_3 + k_4}{6}$$

**Pseudocódigo:**
```text
ALGORITMO RK4
    ENTRADA: f, t0, y0, tf, h
    MIENTRAS t < tf:
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h,   y + k3  )
        y  = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t  = t + h
FIN ALGORITMO
```

**Orden de error:** $O(h^4)$ — al reducir $h$ a la mitad, el error se reduce 16 veces.  
**Uso recomendado:** Es el método estándar para la mayoría de PVI.

---

## 2. Métodos de Pasos Múltiples

### Adams-Bashforth de 4 Pasos — `Adams_Bashforth/`

Reutiliza evaluaciones anteriores de $f$ para predecir el siguiente paso sin cálculos adicionales.

$$y_{n+1} = y_n + \frac{h}{24}\left(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}\right)$$

**Arranque:** Los primeros 3 pasos se calculan con RK4 (ya que requiere 4 puntos previos).

**Pseudocódigo:**
```text
ALGORITMO AdamsBashforth4
    ENTRADA: f, t0, y0, tf, h
    // Arranque: calcular y1, y2, y3 con RK4
    PARA i DESDE 1 HASTA 3: y[i] = RK4_un_paso(f, t[i-1], y[i-1], h)
    
    // Fase principal
    MIENTRAS t < tf:
        y_nuevo = y[n] + h/24 * (55*f[n] - 59*f[n-1] + 37*f[n-2] - 9*f[n-3])
        t = t + h
FIN ALGORITMO
```

**Ventaja:** Solo 1 evaluación de $f$ por paso (vs 4 en RK4).  
**Desventaja:** Requiere paso fijo; sensible a errores acumulados.

---

## 3. Sistemas de Ecuaciones Diferenciales Ordinarias — `Sistemas_EDO/`

Para EDOs de orden superior o sistemas acoplados, se reformula como sistema de primer orden:

**Ejemplo: Péndulo $\theta'' + \frac{g}{L}\sin\theta = 0$**

Se define $y_1 = \theta$, $y_2 = \theta'$:
$$\begin{cases} y_1' = y_2 \\ y_2' = -\dfrac{g}{L}\sin(y_1) \end{cases}$$

RK4 se extiende naturalmente vectorialmente aplicando las mismas 4 pendientes a cada componente.

**Pseudocódigo:**
```text
ALGORITMO RK4_Sistema
    ENTRADA: F (vectorial), t0, Y0[], tf, h
    MIENTRAS t < tf:
        K1 = F(t,       Y          )
        K2 = F(t + h/2, Y + K1*h/2 )
        K3 = F(t + h/2, Y + K2*h/2 )
        K4 = F(t + h,   Y + K3*h   )
        Y  = Y + (K1 + 2*K2 + 2*K3 + K4) * h/6
        t  = t + h
FIN ALGORITMO
```

---

## Comparativa de Métodos

| Método | Evaluaciones de $f$/paso | Orden | Mejor para |
|--------|:------------------------:|:-----:|------------|
| Euler | 1 | $O(h)$ | Demostración, no para producción |
| RK4 | 4 | $O(h^4)$ | Uso general, estándar de facto |
| Adams-Bashforth 4 | 1 (más arranque) | $O(h^4)$ | Problemas con $f$ muy costosa |

---

## Notas de Implementación

- **Estabilidad:** Euler y Adams-Bashforth son **explícitos** y pueden volverse inestables para EDOs rígidas (*stiff*). Para esos casos se usan métodos implícitos como Crank-Nicolson o BDF.
- **Control de paso adaptativo:** En la práctica, RK4 se combina con un estimador de error (RK45) que ajusta $h$ automáticamente (implementado en `scipy.integrate.solve_ivp`).
- **Precisión vs. tiempo:** Para la mayoría de aplicaciones de ingeniería, **RK4 con $h$ moderado es la mejor elección** en relación precisión/costo.
