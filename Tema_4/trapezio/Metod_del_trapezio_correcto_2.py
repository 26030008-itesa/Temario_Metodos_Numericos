import math

def funcion(x):
    """
    Función que deseamos integrar.
    En este caso: f(x) = sin(x)
    """
    return math.sin(x)

def simpson_13_simple(f, a, b):
    """
    Aproxima la integral en el intervalo [a, b] usando la Regla de Simpson 1/3 Simple.
    Requiere evaluar la función en los extremos y exactamente en el punto medio.
    """
    punto_medio = (a + b) / 2.0
    
    # La fórmula asigna un peso de 4 al nodo central y divide el ancho entre 6
    area = ((b - a) / 6.0) * (f(a) + 4 * f(punto_medio) + f(b))
    return area

def simpson_13_compuesto(f, a, b, n):
    """
    Aproxima la integral usando la Regla de Simpson 1/3 Compuesta.
    
    Parámetros:
    f : Función a integrar
    a : Límite inferior
    b : Límite superior
    n : Número de particiones (¡DEBE SER UN NÚMERO PAR!)
    """
    # En Simpson 1/3, el número de subintervalos debe ser par obligatoriamente
    if n % 2!= 0:
        raise ValueError("Error: El número de subintervalos 'n' debe ser par.")
        
    h = (b - a) / n
    suma = f(a) + f(b)
    
    # Agrupamos los puntos interiores
    for i in range(1, n):
        x_i = a + i * h
        # Los índices pares se multiplican por 2 y los impares por 4
        if i % 2 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 4 * f(x_i)
            
    # Multiplicamos todo por h/3 (de ahí el nombre de la regla)
    area = (h / 3.0) * suma
    return area

if __name__ == "__main__":
    # --- Configuración del problema ---
    limite_inferior = 0.0
    limite_superior = math.pi
    
    # Asignamos 6 subintervalos (es un número par, por lo que es correcto)
    subintervalos = 6
    valor_exacto = 2.0
    
    # --- Ejecución de los algoritmos ---
    resultado_simple = simpson_13_simple(funcion, limite_inferior, limite_superior)
    resultado_compuesto = simpson_13_compuesto(funcion, limite_inferior, limite_superior, subintervalos)
    
    # --- Impresión de Resultados ---
    print("=== MÉTODO DE INTEGRACIÓN NUMÉRICA: SIMPSON 1/3 ===")
    print(f"Integrando f(x) = sin(x) desde a = {limite_inferior:.4f} hasta b = {limite_superior:.4f}")
    print(f"Valor analítico exacto esperado: {valor_exacto:.6f}\n")
    
    print("1. Regla de Simpson 1/3 Simple (Evalúa los 2 extremos y 1 punto medio):")
    error_simple = abs(valor_exacto - resultado_simple)
    print(f"   Resultado : {resultado_simple:.6f}")
    print(f"   Error abs : {error_simple:.6f}\n")
    
    print(f"2. Regla de Simpson 1/3 Compuesta (con n = {subintervalos} subintervalos pares):")
    error_compuesto = abs(valor_exacto - resultado_compuesto)
    print(f"   Resultado : {resultado_compuesto:.6f}")
    print(f"   Error abs : {error_compuesto:.6f}")