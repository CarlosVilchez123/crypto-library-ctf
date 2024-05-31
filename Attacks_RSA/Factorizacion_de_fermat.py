import gmpy2
from gmpy2 import mpz

def fermat_factorization(n):
    if n % 2 == 0:
        raise ValueError("El método de factorización de Fermat solo se aplica a números impares.")

    a = gmpy2.isqrt(n) + 1
    b2 = a * a - n
    b = gmpy2.isqrt(b2)

    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = gmpy2.isqrt(b2)

    p = a + b
    q = a - b

    return int(p), int(q)
