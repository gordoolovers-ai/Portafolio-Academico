import numpy as np

# Definimos las funciones para cada variable
def calc_x(y, z):
    return (960 - 3*y - 2*z) / 4

def calc_y(x, z):
    return (510 - x - z) / 3

def calc_z(x, y):
    return (610 - 2*x - y) / 3

# Valores iniciales
x_old, y_old, z_old = 0, 0, 0  # Aproximación inicial
tolerance = 0.01  # Criterio de convergencia ajustado
max_iterations = 1000  # Máximo número de iteraciones

# Iteración
for i in range(max_iterations):
    # Cálculo de las nuevas aproximaciones
    x_new = calc_x(y_old, z_old)
    y_new = calc_y(x_old, z_old)
    z_new = calc_z(x_old, y_old)
    
    # Calculamos el error (diferencia entre los valores nuevos y antiguos)
    error_x = abs(x_new - x_old)
    error_y = abs(y_new - y_old)
    error_z = abs(z_new - z_old)
    
    # Mostramos los resultados en cada iteración
    print(f"Iteration {i+1}: x = {x_new:.5f}, y = {y_new:.5f}, z = {z_new:.5f}")
    print(f"Errors: error_x = {error_x:.5f}, error_y = {error_y:.5f}, error_z = {error_z:.5f}")
    
    # Verificamos la convergencia
    if error_x <= tolerance and error_y <= tolerance and error_z <= tolerance:
        print(f"Converged after {i+1} iterations")
        break
    
    # Actualizamos los valores para la siguiente iteración
    x_old, y_old, z_old = x_new, y_new, z_new

# Mostramos los resultados finales
print(f"Final solution: x = {x_new:.5f}, y = {y_new:.5f}, z = {z_new:.5f}")
