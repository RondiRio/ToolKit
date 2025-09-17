def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Lista de primos no intervalo [10000, 20000]
primes = []

for i in range(100000000, 200000000):
    if is_prime(i):
        primes.append(i)

# Print dos primos encontrados
for prime in primes:
    print(f"É primo {prime}")
