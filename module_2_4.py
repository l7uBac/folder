numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in numbers[1:16]:
    for j in range(2, i-1):
        if i % j == 0:
            not_primes.append(i)
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    is_prime = True

print('primes', primes)
print('not_primes', not_primes)