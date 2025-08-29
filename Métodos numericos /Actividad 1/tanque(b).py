import numpy as np

# Definimos la función f(h) y su derivada f'(h)
def f(h):
    R = 3  # Radio del tanque en metros
    V = 30  # Volumen deseado en m^3
    return V - (np.pi / 3) * h**2 * (3 * R - h)

def f_prime(h):
    R = 3  # Radio del tanque en metros
    return -(np.pi / 3) * (3 * h * (6 - h))

# Método de Newton-Raphson
def newton_raphson(initial_guess, iterations):
    h_n = initial_guess
    for i in range(iterations):
        f_h_n = f(h_n)
        f_prime_h_n = f_prime(h_n)

        if f_prime_h_n == 0:  # Evitar división por cero
            print("La derivada es cero. No se puede continuar.")
            return None

        h_next = h_n - f_h_n / f_prime_h_n

        # Calcular el error relativo aproximado
        error_relative = abs((h_next - h_n) / h_next) if h_next != 0 else float('inf')

        print(f"Iteración {i + 1}:")
        print(f"h_{i} = {h_n:.6f}, h_{i+1} = {h_next:.6f}, Error relativo ≈ {error_relative:.6%}")

        h_n = h_next

    return h_n

# Parámetros iniciales
initial_guess = 2.5  # Valor inicial para la profundidad
iterations = 3       # Número de iteraciones

# Ejecutar el método de Newton-Raphson
resultado_final = newton_raphson(initial_guess, iterations)