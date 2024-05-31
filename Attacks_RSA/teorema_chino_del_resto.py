def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
    
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
