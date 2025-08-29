def fact(n):
    '''Returns the factorial of n'''
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        f = n*(fact(n-1))
        return f 
    
def combn(n, r):
    '''Returns the number of combinations of n items taken r at a time'''
    if n == r:
        return 1
    elif r == 0:
        return 1
    else:
        c = fact(n)/((fact(n - r))*fact(r))
        return c 
