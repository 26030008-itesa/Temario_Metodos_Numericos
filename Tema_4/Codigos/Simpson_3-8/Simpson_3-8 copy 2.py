import math

def funcion(x):
    """
    Función que deseamos integrar.
    En este caso: f(x) = sin(x)
    """
    return math.sin(x)

def simpson_38_simple(f, a, b):
    """
    Aproxima la integral en el intervalo [a, b] usando la Regla de Simpson 3/8 Simple.
    Requiere dividir el intervalo principal en 3 partes iguales (4 puntos evaluativos).
    """
    h = (b - a) / 3.0
    
    # Calculamos los puntos internos
    x1 = a + h
    x2 = a + 2 * h
    
    # La fórmula asigna un peso de 3 a los nodos internos y multiplica todo por 3h/8
    area = (3.0 * h / 8.0) * (f(a) + 3 * f(x1) + 3 * f(x2) + f(b))
    return area

def simpson_38_compuesto(f, a, b, n):
    """
    Aproxima la integral usando la Regla de Simpson 3/8 Compuesta.
    
    Parámetros:
    f : Función a integrar
    a : Límite inferior
    b : Límite superior
    n : Número de particiones (¡DEBE SER MÚLTIPLO DE 3!)
    """
    # En Simpson 3/8, el número de subintervalos debe ser obligatoriamente un múltiplo de 3
    if n % 3!= 0:
        raise ValueError("Error: El número de subintervalos 'n' debe ser un múltiplo de 3.")
        
    h = (b - a) / n
    suma = f(a) + f(b)
    
    # Agrupamos y ponderamos los puntos interiores
    for i in range(1, n):
        x_i = a + i * h
        
        # Si el índice es múltiplo de 3, el coeficiente multiplicador es 2
        if i % 3 == 0:
            suma += 2 * f(x_i)
        # Para el resto de los índices internos, el coeficiente es 3
        else:
            suma += 3 * f(x_i)
            
    # Multiplicamos la sumatoria total por el factor escalar 3h/8
    area = (3.0 * h / 8.0) * suma
    return area

if __name__ == "__main__":
    # --- Configuración del problema ---
    limite_inferior = 0.0
    limite_superior = math.pi
    
    # Asignamos 6 subintervalos (es múltiplo de 3, por lo que el algoritmo funcionará)
    subintervalos = 6
    valor_exacto = 2.0
    
    # --- Ejecución de los algoritmos ---
    resultado_simple = simpson_38_simple(funcion, limite_inferior, limite_superior)
    resultado_compuesto = simpson_38_compuesto(funcion, limite_inferior, limite_superior, subintervalos)
    
    # --- Impresión de Resultados ---
    print("=== MÉTODO DE INTEGRACIÓN NUMÉRICA: SIMPSON 3/8 ===")
    print(f"Integrando f(x) = sin(x) desde a = {limite_inferior:.4f} hasta b = {limite_superior:.4f}")
    print(f"Valor analítico exacto esperado: {valor_exacto:.6f}\n")
    
    print("1. Regla de Simpson 3/8 Simple (Evalúa 4 puntos espaciados):")
    error_simple = abs(valor_exacto - resultado_simple)
    print(f"   Resultado : {resultado_simple:.6f}")
    print(f"   Error abs : {error_simple:.6f}\n")
    
    print(f"2. Regla de Simpson 3/8 Compuesta (con n = {subintervalos} subintervalos):")
    error_compuesto = abs(valor_exacto - resultado_compuesto)
    print(f"   Resultado : {resultado_compuesto:.6f}")
    print(f"   Error abs : {error_compuesto:.6f}")