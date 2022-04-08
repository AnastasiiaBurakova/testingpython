from math import sqrt 
def is_prime(n):
    if n > 1:    
        for i in range (2, int(sqrt(n))+1):
            if (n % i) == 0:
                return False
        else:
            return True     
    else:
        return False   

def primes_below(n):
    l = []
    for i in range (2, n):
        if is_prime(i):
            l.append(i)
    return l           

def palindrome_primes():
    l = []
    for i in range (10000, 100000):
        if str(i) == str(i)[::-1]:
            if is_prime(i):
                l.append(i)
    return l


