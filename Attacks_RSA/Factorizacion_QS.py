import sympy
import math
import numpy as np
from sympy import Matrix

def quadratic_sieve(n):
    def is_quadratic_residue(a, p):
        return pow(a, (p - 1) // 2, p) == 1
    
    def find_smooth_base(n, limit):
        primes = list(sympy.primerange(2, limit))
        base = [p for p in primes if is_quadratic_residue(n, p)]
        return base
    
    def generate_polynomials(n, base):
        sqrt_n = math.isqrt(n)
        m = len(base)
        B = [math.isqrt(p * n) for p in base]
        polynomials = [(a, (a * a - n) % n) for a in B]
        return polynomials
    
    def factor_base_expansion(x, base):
        factors = [0] * len(base)
        for i, p in enumerate(base):
            while x % p == 0:
                x //= p
                factors[i] += 1
        return factors if x == 1 else None
    
    def find_smooth_numbers(n, base, polynomials):
        smooth_numbers = []
        for a, b in polynomials:
            b_expansion = factor_base_expansion(b, base)
            if b_expansion is not None:
                smooth_numbers.append((a, b, b_expansion))
        return smooth_numbers
    
    def solve_matrix(smooth_numbers, base):
        m = len(smooth_numbers)
        n = len(base)
        matrix = np.zeros((m, n), dtype=int)
        for i, (_, _, exp) in enumerate(smooth_numbers):
            matrix[i] = exp
        matrix = Matrix(matrix).rref()[0]
        return matrix
    
    def find_factors(n, smooth_numbers, matrix):
        for row in matrix.tolist():
            lhs = 1
            rhs = 1
            for i, exp in enumerate(row):
                if exp % 2 == 1:
                    lhs = (lhs * smooth_numbers[i][0]) % n
                    rhs = (rhs * smooth_numbers[i][1]) % n
            factor = math.gcd(lhs - math.isqrt(rhs), n)
            if factor not in [1, n]:
                return factor, n // factor
        return None
    
    B = 1000000  # Limite de la base
    base = find_smooth_base(n, B)
    polynomials = generate_polynomials(n, base)
    smooth_numbers = find_smooth_numbers(n, base, polynomials)
    
    if len(smooth_numbers) < len(base):
        raise ValueError("No se encontraron suficientes números suaves.")
    
    matrix = solve_matrix(smooth_numbers, base)
    factors = find_factors(n, smooth_numbers, matrix)
    
    if factors:
        return factors
    else:
        raise ValueError("No se encontraron factores.")


n = 13*7  
p, q = quadratic_sieve(n)
print(f'Los factores de {n} son {p} y {q}')