import numpy as np

def division_polynomials(dividendo, divisor):
    dividendo = np.array(dividendo, dtype=float)
    divisor = np.array(divisor, dtype=float)

    grado_dividiendo = len(dividendo) -1
    grado_divisor = len(divisor) -1

    cociente = np.zeros(grado_dividiendo - grado_divisor +1)
    resto = dividendo.copy()

    for i in range(grado_dividiendo - grado_divisor +1):
        coeficiente = resto[i]/divisor[0]
        cociente[i] = coeficiente
        for j in range(len(divisor)):
            resto[i+j] -= coeficiente*divisor[j]
    # aqui solamente estamos eliminando los ceros del divisor
    resto = np.trim_zeros(resto, 'f')

    return cociente, resto

def gcd_extend_polynomials(p, q):
    u = np.array(p, dtype=float)
    v = np.array(q, dtype=float)
    x1, x2 = np.array([1.0]), np.array([0.0])
    y1, y2 = np.array([0.0]), np.array([1.0])
    while not np.all(v == 0):
        cociente , resto = division_polynomials(u, v)
        u, v = v, resto
        x1, x2 = x2, np.polysub(x1, np.polymul(cociente, x2))
        y1, y2 = y2, np.polysub(y1, np.polymul(cociente, y2))
        #print(f'{u}, {resto}')

    return u, x1, y1