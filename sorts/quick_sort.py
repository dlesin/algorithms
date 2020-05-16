""" Сортировка Тони Хоара (быстрая) """

def quick_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []; M = []; R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

def test_sorts(sort_algo):
    print("test #1: ", end="")
    A = [4, 2, 3, 5, 1, 7, 6]
    A_sorted = [1, 2, 3, 4, 5, 6, 7]
    sort_algo(A)
    print("Ok" if A == A_sorted else "Fail")

    print("test #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algo(A)
    print("Ok" if A == A_sorted else "Fail")

    print("test #3: ", end="")
    A = [4, 2, 2, 3, 1, 5, 1, 3, 6]
    A_sorted = [1, 1, 2, 2, 3, 3, 4, 5, 6]
    sort_algo(A)
    print("Ok" if A == A_sorted else "Fail")

if __name__ == '__main__':
    test_sorts(quick_sort)