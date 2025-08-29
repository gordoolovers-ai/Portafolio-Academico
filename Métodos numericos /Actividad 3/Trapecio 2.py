import numpy as np

# Introducir la función f(x)
def f(x):
    if x <= 15:
        return 4.5
    elif 15 < x <= 30:
        return 6
    elif 30 < x <= 45:
        return 3.5
    elif 45 < x <= 75:
        return 6
    elif 75 < x <= 105:
        return 5.25
    else:
        return 2.25

# Función para la integral numérica usando el método del trapecio
def metodo_trapecio(f, a, b, n):
    h = (b - a) / n  # Tamaño del intervalo o paso
    suma = (f(a) + f(b)) / 2  # f(a) y f(b) contribuyen una vez
    # Sumar los valores de f en los puntos intermedios
    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

# Valores de los límites de integración y el número de subintervalos
a = 0  # Límite inferior
b = 105  # Límite superior
n = 100  # Número de subintervalos

# Calcular la integral
resultado = metodo_trapecio(f, a, b, n)
print(f"El valor aproximado de la integral es: {resultado}")