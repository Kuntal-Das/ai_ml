def sieve_of_eratosthenes(n):
    # Create a boolean list "prime[0..n]" and initialize
    # all entries as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    
    # Mark all the multiples of each prime number as composite
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    # Return a list of prime numbers up to n
    return [i for i in range(2, n+1) if primes[i]]


primes = sieve_of_eratosthenes(50)
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]