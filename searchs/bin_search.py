""" Бинарный поиск, массив должен быть отсортирован """

def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

if __name__ == '__main__':
    Arr = [i for i in range(20)]
    print('left bound = ', left_bound(Arr, 7))
    print('right bound = ', right_bound(Arr, 7))