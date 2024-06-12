from factorization.GCD_extends import extended_gcd

def CRT(N_list_modules, list_rest):
    sum = 0
    prod = 1
    for ni in N_list_modules:
        prod *=ni
    
    for ni, ai in zip(N_list_modules, list_rest):
        p = prod // ni
        g,x,y = extended_gcd(p,ni)
        if g != 1:
            raise ValueError(b'los modulos no son coprimos')
        sum += ai*x*p
    
    return sum % prod
