import numpy as np

# Valores de x y H dados
x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
H = np.array([0, 1.9, 2, 2, 2.4, 2.6, 2.25, 1.12, 0])

# Función para interpolar los valores
def f(x_val):
    return np.interp(x_val, x, H)

# Método de Romberg
def romberg_integration(f, a, b, tol=0.01):
    R = [[0.5 * (b - a) * (f(a) + f(b))]]
    n = 1
    while True:
        h = (b - a) / (2 ** n)
        sum_f = sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (n - 1) + 1))
        R.append([0.5 * R[n-1][0] + h * sum_f])
        for m in range(1, n + 1):
            R[n].append(R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4 ** m - 1))
        if n > 1 and abs(R[n][n] - R[n-1][n-1]) < tol * abs(R[n][n]):
            return R[n][n]
        n += 1

# Calcula el área usando Romberg
area = romberg_integration(f, 0, 16)
print("El área de la sección transversal del río es:", area)

