import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(y):
    return 1 - (400 / (9.81 * (3 * y + (y**2) / 2)**3)) * (3 + y)

# Generamos valores de y de 0.1 en 0.1
y_values = np.arange(0.5, 2.6, 0.5)
x_values = f(y_values)

# Mostramos cada iteración
for y, x in zip(y_values, x_values):
    print(f'y: {y:.2f}, x: {x:.4f}')

# Graficamos con x en el eje horizontal y y en el eje vertical
plt.plot(x_values, y_values, marker='o')
plt.title('Comportamiento de la función')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
