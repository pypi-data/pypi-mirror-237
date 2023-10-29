def SieveEra(limit=20):
    is_prime = [True] * (limit+1)
    is_prime[0] = is_prime[1] = False
    
    for number in range(2, int(limit**0.5)+1):
        if is_prime[number]:
            for m in range(number**2, limit+1, number):
                is_prime[m] = False
                
    primes = [number for number in range(2, limit+1) if is_prime[number]]
    return primes