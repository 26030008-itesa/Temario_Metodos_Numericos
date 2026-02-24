# Unidad 2: Metodos de solucion de ecuaciones no lineales

---

## Competencia Especifica
Solucionar ecuaciones no lineales mediante los diferentes metodos numericos para aplicarlos en la resolucion de problemas de ingenieria.

---

## Metodos Implementados

### Metodos Cerrados (Intervalos)
Estos metodos requieren de un intervalo inicial [a, b] donde se cumpla el **Teorema de Bolzano** ($f(a) * f(b) < 0$) para garantizar la existencia de al menos una raiz.

1. **Metodo de Biseccion:** Divide sistematicamente el intervalo a la mitad hasta alcanzar la tolerancia deseada.
2. **Metodo de Regla Falsa:** Utiliza una linea secante para aproximar la raiz de forma mas eficiente que la biseccion.
   * Formula: $$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$

### Metodos Abiertos
A diferencia de los metodos cerrados, estos no requieren encerrar la raiz, lo que los hace mas rapidos pero con riesgo de divergencia.

1. **Metodo de Newton-Raphson:** Emplea la derivada de la funcion para proyectar la siguiente aproximacion mediante una recta tangente.
2. **Metodo de la Secante:** Similar a Newton-Raphson pero sustituye la derivada por una aproximacion basada en dos puntos iniciales.

---

## Analisis de Implementacion y Control de Errores

Durante el desarrollo de las practicas en Excel, se identificaron puntos criticos para la correcta ejecucion de los algoritmos:

* **Jerarquia de Operaciones:** En la implementacion de la Regla Falsa en Excel, es mandatorio agrupar el denominador entre parentesis `/(f(a)-f(b))` para evitar que el software realice calculos erroneos y provoque divergencia (error #NUM!).
* **Validacion de Continuidad:** Se demostro que el Teorema de Bolzano es invalido si la funcion presenta discontinuidades o asintotas en el intervalo elegido (ejemplo: x=3 en la funcion 1/(x-3)), lo que puede generar resultados erroneos o "raices fantasmales".
* **Criterio de Parada:** Se utiliza el error relativo porcentual para detener las iteraciones cuando la aproximacion es suficientemente precisa para los requerimientos de ingenieria.

---

## Casos de Prueba
* **Funcion Polinomica:** $2x^2 - 7x$ en el intervalo [2, 4] con raiz real en 3.5.
* **Funcion Trascendente:** $(1/(x-3)) + cos(x)$ analizada para detectar fallos por asintotas verticales.

---
[Volver al menu principal](../README.md)