# Definir la función f(x)
def f(x):
    if  x <= 15:
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

# Método de Simpson
def metodo_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n, 2):  # Para términos impares
        suma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):  # Para términos pares
        suma += 2 * f(a + i * h)

    return (h / 3) * suma

# Valores de los límites de integración y el número de subintervalos
a = 0  # Límite inferior
b = 105  # Límite superior
n = 100 # Número de subintervalos (debe ser par)

# Calcular la integral
resultado = metodo_simpson(f, a, b, n)
print(f"El valor aproximado de la integral es: {resultado:.2f}")
