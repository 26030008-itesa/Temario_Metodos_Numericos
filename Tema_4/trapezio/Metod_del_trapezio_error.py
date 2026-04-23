import math

def funcion(x):
    """
    Función que deseamos integrar.
    En este caso: f(x) = sin(x)
    """
    return math.sin(x)

def trapecio_simple(f, a, b):
    """
    Aproxima la integral de f(x) en el intervalo [a, b] 
    usando la Regla del Trapecio Simple.
    """
    area = (b - a) * (f(a) + f(b)) / 2.0
    return area

def trapecio_compuesto(f, a, b, n):
    """
    Aproxima la integral de f(x) en el intervalo [a, b] 
    usando la Regla del Trapecio Compuesta.
    """
    # Si n = 0, el programa colapsará inmediatamente en esta línea:
    h = (b - a) / n
    
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        suma += 2 * f(x_i)
        
    area = (h / 2.0) * suma
    return area

if __name__ == "__main__":
    # --- Configuración del problema ---
    limite_inferior = 0.0
    limite_superior = math.pi
    
    # ¡AQUÍ PROVOCAMOS EL ERROR CON BASE EN LOS VALORES!
    # Cambiamos n = 6 por n = 0. Matemáticamente es imposible hacer cero particiones.
    subintervalos = 0
    
    valor_exacto = 2.0
    
    print("=== MÉTODO DE INTEGRACIÓN NUMÉRICA: REGLA DEL TRAPECIO ===")
    print(f"Integrando f(x) = sin(x) desde a = {limite_inferior:.4f} hasta b = {limite_superior:.4f}")
    print(f"Número de subintervalos asignados: {subintervalos}\n")
    
    # Ejecutamos el código dentro de un bloque try-except para atrapar el colapso
    try:
        resultado_compuesto = trapecio_compuesto(funcion, limite_inferior, limite_superior, subintervalos)
        print(f"Resultado : {resultado_compuesto:.6f}")
    except Exception as e:
        print("¡ERROR PROVOCADO DETECTADO EN LA EJECUCIÓN!")
        print(f"Tipo de error de Python : {type(e).__name__}")
        print(f"Mensaje del sistema     : {e}")
        print("\nExplicación:")
        print("El algoritmo intentó calcular el tamaño del paso 'h' mediante la operación (b - a) / n.")
        print("Al asignarle a los valores que n = 0, se provocó una división entre cero que destruye la lógica matemática.")