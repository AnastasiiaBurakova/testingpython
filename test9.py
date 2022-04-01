def is_prime(n):
    if n > 1:    
        for i in range (2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True     
    else:
        return False   

def primes_below(n):
    for i in range (2, n + 1):
        if is_prime(i):
            print (i, end = ' ')       