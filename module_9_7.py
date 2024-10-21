def is_prime(func):
    def wrapper(*args, **kwargs):
        sum2 = func(*args, **kwargs)
        d = 2
        while sum2 % d != 0:
            d += 1
        if sum2 == d:
            print('Простое число')
        else:
            print('Составное число')
        return d

    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
