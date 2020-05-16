""" Вычисление чисел Фибоначчи """

def fib(n):
    """ Фибоначчиево дерево О(Fib n) супер долгое """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fast_fib(n):
    """ Быстрый вариант - динамическое программирование"""
    fib = [0, 1] + [0] * n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

n = 5
print ("fast_fib - ", fast_fib(n))
print ("fib - ", fib(n))