def bubble_sort_for(A):
    n = len(A)
    while n > 1 :
        for i in range(0, n-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        n = n-1


def bubble_sort(A):
    n = len(A)
    while n > 1:
        i = 0
        while i < n-1:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
            i = i+1
        n = n-1

def bubble_sort_invert(A):
    n = len(A)
    s = 0
    while s < n-1:
        i = n-1
        while i > s:
            if A[i] > A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                print(A)
            i = i-1
        s = s+1


Liste = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(Liste)
print(Liste)