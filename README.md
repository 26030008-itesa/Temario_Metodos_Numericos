# Metodos Numericos (SCC-1017)
## Ingenieria en Sistemas Computacionales | ITESA
**Estudiante:** Cristian

Este repositorio ha sido desarrollado para documentar y organizar las practicas, investigaciones y algoritmos correspondientes a la asignatura de **Metodos Numericos**. El contenido se enfoca en la aplicacion de modelos matematicos y su resolucion mediante aproximaciones numericas procesadas en herramientas computacionales.

---

## Estructura del Repositorio
El curso se divide en cinco unidades tematicas. Cada carpeta contiene la documentacion teorica y los archivos de implementacion (Excel o codigo) respectivos.

| Unidad | Titulo | Descripcion |
| :--- | :--- | :--- | 
| [**Unidad 1**](./Tema%201/) | Introduccion a los metodos numericos | Analisis de tipos de errores, precision y cifras significativas. | 
| [**Unidad 2**](./Tema_2/) | Ecuaciones no lineales | Implementacion de metodos de intervalos (Biseccion, Regla Falsa) y metodos abiertos. | 
| **Unidad 3**(./Tema_3)|  Sistemas de ecuaciones lineales | Solucion de sistemas mediante metodos directos e iterativos. | Pendiente |
| **Unidad 4** | Diferenciacion e integracion numerica | Tecnicas de aproximacion para derivadas e integrales definidas. | Pendiente |
| **Unidad 5** | Ecuaciones diferenciales | Metodos de solucion para problemas de valor inicial. | Pendiente |

---

## Tecnologias y Herramientas
Para garantizar la precision de los calculos y la validacion de los resultados, se emplean las siguientes herramientas:

* **Hojas de Calculo (Excel / ODS):** Utilizadas para la creacion de tablas de iteracion, calculo de error relativo porcentual y aplicacion de funciones logicas para la actualizacion de limites.
* **GeoGebra:** Empleado como herramienta de soporte grafico para visualizar el comportamiento de las funciones y verificar la existencia de raices antes de la implementacion numerica.
* **Software de Programacion:** Desarrollo de algoritmos de ingenieria para la automatizacion de procesos numericos.

---

## Metodologia de Trabajo
Las actividades desarrolladas en este repositorio siguen un rigor academico basado en los siguientes puntos:

1. **Analisis de Continuidad:** Antes de aplicar metodos cerrados, se verifica la continuidad de la funcion en el intervalo seleccionado para evitar errores por asintotas o discontinuidades.
2. **Teorema de Bolzano:** Se valida que exista un cambio de signo ($f(a) * f(b) < 0$) para garantizar la convergencia de los metodos de Biseccion y Regla Falsa.
3. **Analisis de Error:** Se monitorea el error relativo porcentual en cada iteracion para determinar el momento exacto en que la aproximacion cumple con la tolerancia requerida.

