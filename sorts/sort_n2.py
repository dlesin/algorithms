def insert_sort(A):
    """
    Сортировка вставкой, путём прохода по массиву поеском меньшего и вставкой в позиции по очереди
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1 


def select_sort(A):
    """
    Сортировка выбором, путём выбора позиции и проходом по всему массиву, поиском мешего. Далешь следующий
    """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """
    Сортировка пузырьком, путём сравнением 2х позиций и заменой их местами. В итоге в право уедет самы старший
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


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
    test_sorts(insert_sort)
    test_sorts(select_sort)
    test_sorts(bubble_sort)