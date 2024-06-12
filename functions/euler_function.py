from factrizaciones.GCD_extends import *
def euler_function(n):
    numbers_coprimes = 1
    for i in range(2, n):
        if extended_gcd(i,n)[0] == 1:
            numbers_coprimes +=1
    
    return numbers_coprimes
