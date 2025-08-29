import math

Bi=0.5
max = 50
incm = 0.1
tol = 1e-6
it = 1000
rootb = [0] * max

def f(x):
    return x*math.tan(x)-Bi

with open('Beta.dat', 'w') as file:
    for r in range(1, max+1):
        n = r - 1
        m = n * math.pi
        xx = [0] * 1000
        xx[0] = m + 0.01
        xx[1] = m + 1
        for i in range(1, it+1):
            f1 = f(xx[i])
            f2 = f(xx[i-1])
            xx[i+1] = xx[i] - (f1 * ((xx[i] - xx[i-1]) / (f1 - f2)))
            if abs(xx[i+1] - xx[i]) < tol:
                rootb[r-1] = abs(xx[i+1])
                break
        file.write(f"{r:10} {rootb[r-1]:10.5f}\n")

if i > it:
    print('No se halló raíz: cambiar aprox. iniciales o aumentar ITER_MAX')
    
    


