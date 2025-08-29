def f(y):
    return 1 - (400 / (9.81 * (3 * y + (y**2 / 2))**3)) * (3 + y)

def bisection_method(xl, xu, tol=0.01, max_iter=10):
    if f(xl) * f(xu) >= 0:
        print("No se puede aplicar el método de bisección.")
        return None
    
    iter_count = 0
    print(f"{'Iteración':<10}{'xl':<10}{'xu':<10}{'c':<10}{'f(c)':<10}")
    
    while iter_count < max_iter:
        c = (xl + xu) / 2
        error = abs((xu - xl) / 2)
        
        # Imprimir la información de la iteración
        print(f"{iter_count + 1:<10}{xl:<10.5f}{xu:<10.5f}{c:<10.5f}{f(c):<10.5f}")
        
        if f(c) == 0 or error < tol * abs(c):
            return c  # Encontramos la raíz o cumplimos la tolerancia
        
        if f(xl) * f(c) < 0:
            xu = c
        else:
            xl = c
            
        iter_count += 1

    return (xl + xu) / 2

# Intervalo inicial
xl = .5
xu = 2.5
tolerance = 0.01

raiz = bisection_method(xl, xu, tolerance)
print(f"La raíz es aproximadamente: {raiz:.5f}")
