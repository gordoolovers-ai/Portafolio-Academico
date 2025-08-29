import numpy as np

# Introducir los coeficientes del sistema de ecuaciones en forma matricial
A = np.array([[6, 5, 3, 2],
              [2, 5, 2, 3],
              [4, 3, 4, 1],
              [1, 2, 3, 4]])

b = np.array([920, 550, 620, 400])

# valores iniciales para x1, x2, x3, x4, todos igual con cero
x = np.zeros(4)

# Define el número de iteraciones y la tolerancia 
max_iterations = 100
tolerance = 1e-10

# Aplicación del Método de Gauss-Seidel
for iteration in range(max_iterations):
    x_new = np.copy(x)
    
    # Actualización de las variables calculadas en una iteración anterior
    for i in range(A.shape[0]):
        sum_Ax = np.dot(A[i, :], x_new) - A[i, i] * x_new[i]
        x_new[i] = (b[i] - sum_Ax) / A[i, i]
    
    # Criterio de convergencia
    if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
        print(f'Convergió después de {iteration+1} iteraciones')
        break
    
    x = x_new

# Imprimir los valores de x1,x2,x3,x4
print(f'Solución aproximada:')
print(f'x1 = {x[0]:.6f}')
print(f'x2 = {x[1]:.6f}')
print(f'x3 = {x[2]:.6f}')
print(f'x4 = {x[3]:.6f}')

