def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

def nth_prime(n):
    prime = 2
    while(n != 0):
        prime += 1
        while not is_prime(prime):
            prime += 1
        n -= 1
    return prime
