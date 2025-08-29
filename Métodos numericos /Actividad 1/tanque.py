{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import numpy as np\
\
# Definimos la funci\'f3n f(h) y su derivada f'(h)\
def f(h):\
    R = 3  # Radio del tanque en metros\
    V = 30  # Volumen deseado en m^3\
    return V - (np.pi / 3) * h**2 * (3 * R - h)\
\
def f_prime(h):\
    R = 3  # Radio del tanque en metros\
    return -(np.pi / 3) * (3 * h * (6 - h))\
\
# M\'e9todo de Newton-Raphson\
def newton_raphson(initial_guess, iterations):\
    h_n = initial_guess\
    for i in range(iterations):\
        f_h_n = f(h_n)\
        f_prime_h_n = f_prime(h_n)\
\
        if f_prime_h_n == 0:  # Evitar divisi\'f3n por cero\
            print("La derivada es cero. No se puede continuar.")\
            return None\
\
        h_next = h_n - f_h_n / f_prime_h_n\
\
        # Calcular el error relativo aproximado\
        error_relative = abs((h_next - h_n) / h_next) if h_next != 0 else float('inf')\
\
        print(f"Iteraci\'f3n \{i + 1\}:")\
        print(f"h_\{i\} = \{h_n:.6f\}, h_\{i+1\} = \{h_next:.6f\}, Error relativo \uc0\u8776  \{error_relative:.6%\}")\
\
        h_n = h_next\
\
    return h_n\
\
# Par\'e1metros iniciales\
initial_guess = 2.5  # Valor inicial para la profundidad\
iterations = 3       # N\'famero de iteraciones\
\
# Ejecutar el m\'e9todo de Newton-Raphson\
resultado_final = newton_raphson(initial_guess, iterations)\
}