

def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    print ('pivot -', pivot )
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    print ('less', less)
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    print ('greater', greater)
    return quicksort(less) + [pivot] + quicksort(greater)

print('qsort -', quicksort([33, 13, 10, 5, 2, 3, 6, 12, 99, 44, 66, 23, 89]))
