import math

# Definir la funcion del problema del coeficiente de arrastre
def f(c):
    return (667.38 / c) * (1 - math.exp(-0.146843 * c)) - 40

# Parámetros del método
a = 8  # Límite inferior del intervalo
b = 20  # Límite superior del intervalo
tolerancia = 0.01

# Este es el método de bisección
def biseccion(a, b, tolerancia):
    # Comprobar que el intervalo es válido
    if f(a) * f(b) >= 0:
        print("El intervalo no es válido. f(a) y f(b) deben tener signos opuestos.")
        return None

    # Variables iniciales
    error = b - a
    iteracion = 0

    # Aplicar el método de bisección
    while error > tolerancia:
        c = (a + b) / 2  # Punto medio
        fc = f(c)
        
        print(f"Iteración {iteracion}: c = {c}, f(c) = {fc}")

        # Verificar si hemos encontrado la raíz con la tolerancia deseada
        if abs(fc) < tolerancia:
            return c
        
        # Determinar en qué subintervalo está la raíz
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        # Actualizar el error y el contador de iteraciones
        error = b - a
        iteracion += 1

    # Devolver la raíz aproximada
    return (a + b) / 2



# Ejecutar el método de bisección
raiz = biseccion(a, b, tolerancia)
if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")