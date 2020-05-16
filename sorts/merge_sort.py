def merge(A:list, B:list):
    """ Сортирующие действие """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]

def test_sorts(sort_algo):
    print("test #1: ", end="")
    A = [4, 2, 3, 5, 1]
    A_sorted = [1, 2, 3, 4, 5]
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
    test_sorts(merge_sort)