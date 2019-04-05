def selection_sort_for(A):
    n = len(A)
    for i in range(0, n-1):
        kleinste = i
        for j in range(i + 1, n):
            if A[j] < A[kleinste]:
                kleinste = j
        A[kleinste], A[i] = A[i] ,A[kleinste]


def selection_sort(A):
    n = len(A)
    i = 0
    while i < n-1:
        kleinste = i
        j = i+1
        while j < n:
            if A[j] < A[kleinste]:
                kleinste = j
            print(A, i, j, kleinste)
            j = j+1
        A[kleinste], A[i] = A[i] ,A[kleinste]
        i = i+1


#Liste = [6,9,3,5,2]
Liste = [9,10,4,3]
selection_sort(Liste)
print(Liste)