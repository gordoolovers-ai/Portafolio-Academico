import numpy as np

# Definimos la función para el método de Gauss-Seidel
def gauss_seidel(A, b, x0, tol=0.01, max_iter=1000):
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])  # Suma de los términos anteriores
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])  # Suma de los términos posteriores
            x[i] = (b[i] - sum1 - sum2) / A[i, i]  # Actualizamos x[i]

        # Calculamos los errores individuales
        errors = np.abs(x - x_old)

        # Imprimimos los resultados
        print(f"Iteración {k + 1}: x = {x}, Errores: x = {errors[0]:.4f}, y = {errors[1]:.4f}, z = {errors[2]:.4f}")

        # Verificamos la condición de convergencia
        if np.max(errors) < tol:
            print("Convergencia alcanzada.")
            return x

    print("Número máximo de iteraciones alcanzado.")
    return x

# Coeficientes del sistema Ax = b
A = np.array([[4, 3, 2],
              [1, 3, 1],
              [2, 1, 3]], dtype=float)

b = np.array([960, 510, 610], dtype=float)

# Valor inicial
x0 = np.zeros(len(b))

# Ejecutamos el método
solution = gauss_seidel(A, b, x0)

print("Solución final:", solution)
