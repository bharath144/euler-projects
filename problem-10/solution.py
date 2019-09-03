def is_prime(num):
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while pow(i, 2) <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False

        i = i + 6

    return True


def get_primes(upper):
    primes = list()
    for i in range(1, upper + 1):
        if is_prime(i):
            primes.append(i)

    return primes


def get_sum_of_primes(upper):
    sum = 0
    for i in range(1, upper + 1):
        if is_prime(i):
            sum = sum + i
            print(sum)

    return sum


print(get_sum_of_primes(2000000)) # 142913828922
