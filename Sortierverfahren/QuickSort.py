def partition(A, start, end):
    pos = start
    for i in range(start, end):
        if A[i] < A[end]:
            A[i], A[pos] = A[pos], A[i]
            pos += 1
    A[pos], A[end] = A[end], A[pos]
    return pos


def quick_sort(A, start, end):
    if start < end:
        pos = partition(A, start, end)
        quick_sort(A, start, pos - 1)
        quick_sort(A, pos + 1, end)
    return A


#unsortierte_Liste = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(quickSort(unsortierte_Liste, 0, len(unsortierte_Liste) - 1))
