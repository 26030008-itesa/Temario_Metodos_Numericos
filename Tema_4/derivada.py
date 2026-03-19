def derivada(f, x, h=1e-7):
    return (f(x + h) - f(x)) / h
def mi_funcion(x):
    return x**2

resultado = derivada(mi_funcion, 5)
print(f"La derivada en x=5 es aproximadamente: {resultado}")