def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M - 1, prefix + digit)


def generate_numbers(N: int, M: int, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


# gen_bin(3)
generate_numbers(4, 4)
