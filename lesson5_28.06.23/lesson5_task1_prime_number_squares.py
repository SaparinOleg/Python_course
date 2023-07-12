def to_sqr(number):
    return number * number


def is_prime(number):
    for i in range(2, number // 2):
        if not number % i:
            return False
    return True


# print([to_sqr(i) for i in range(0, 50) if is_prime(i)])
print(list(map(to_sqr, filter(is_prime, range(0, 50)))))
