from gmpy2 import *
from Functions.euler_function import euler_function
from factrizaciones.GCD_extends import extended_gcd

"""
Remember that the theorems only work if "a" and "n" are comprimes
"""

def euler_theorem(a, n):
    phi = euler_function(n)

    if extended_gcd(a, n)[0] != 1:
        return False

    if gmpy2.powmod(a, phi, n) == 1:
        return True
    return False
    