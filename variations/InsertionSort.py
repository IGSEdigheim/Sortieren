def insertion_sort_for(A):
    n = len(A)
    for i in range(1, n):
        merke = A[i]
        j = i
        while j > 0 and A[j - 1] > merke:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = merke


def insertion_sort_slow(A):
    n = len(A)
    i = 1
    while i < n:
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
        i = i + 1


def insertion_sort(A):
    n = len(A)
    i = 1
    while i < n:
        merke = A[i]
        j = i
        while j > 0 and A[j-1] > merke:
            print(A, i, j, merke)
            A[j] = A[j-1]
            j = j-1
        A[j] = merke
        i = i+1


Liste = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(Liste)
print(Liste)