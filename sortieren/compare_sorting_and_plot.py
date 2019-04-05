import random
from time import *
import sys
import matplotlib.pyplot as plt


def bubble_sort(A) :
    n = len(A)
    while n > 1 :
        i = 0
        while i < n-1:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
            i = i+1
        n = n-1


def selection_sort(A):
    n = len(A)
    i = 0
    while i < n-1:
        kleinste = i
        j = i+1
        while j < n:
            if A[j] < A[kleinste]:
                kleinste = j
            j = j+1
        A[kleinste], A[i] = A[i] ,A[kleinste]
        i = i+1


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
            A[j] = A[j-1]
            j = j-1
        A[j] = merke
        i = i+1


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


maximum = 10001
sys.setrecursionlimit(maximum+2)

# Erzeuge umgekehrt sortierte Liste von Zahlen
#liste = list(range(maximum,0,-1))
#plt.title('Umgekehrt sortierte Zahlenliste')

# Erzeuge zufällige Liste von Zahlen
liste = random.sample(range(maximum), maximum)
plt.title('Zufällige Zahlenliste ohne Wiederholungen')

# Lade Datei mit vielen Zeilen zum sortieren
# with open('pw/10-kilo-pw.txt', 'rt', encoding="ISO-8859-1") as f:  #'10-million-pw.txt'
#     liste = f.read().splitlines()
# plt.title('Zufällige Zeichenfolgen')

x_values = []
y_bubble_sort = []
y_selection_sort = []
# y_insertion_sort_slow = []
y_insertion_sort = []
y_quick_sort = []
y_py_sort = []

for length in range (0, maximum, maximum // 20):
    x_values.append(length)

    # t1 = time()
    # print("bubble_sort,         ", end='')
    # bubble_sort(liste[:length])
    # t2 = time()
    # print(length, ",", t2 - t1)
    # y_bubble_sort.append(t2 - t1)
    #
    # t1 = time()
    # print("selection_sort,      ", end='')
    # selection_sort(liste[:length])
    # t2 = time()
    # print(length, ",", t2 - t1)
    # y_selection_sort.append(t2 - t1)

    # t1 = time()
    # print("insertion_sort_slow, ", end='')
    # insertion_sort_slow(liste[:length])
    # t2 = time()
    # print(length, ",", t2 - t1)
    # y_insertion_sort_slow.append(t2 - t1)

    # t1 = time()
    # print("insertion_sort,      ", end='')
    # insertion_sort(liste[:length])
    # t2 = time()
    # print(length, ",", t2 - t1)
    # y_insertion_sort.append(t2 - t1)

    t1 = time()
    print("quick_sort,          ", end='')
    quick_sort(liste[:length], 0, len(liste[0:length]) - 1)
    t2 = time()
    print(length, ",", t2 - t1)
    y_quick_sort.append(t2 - t1)

    t1 = time()
    print("pythons timsort,     ", end='')
    liste[:length].sort()
    t2 = time()
    print(length, ",", t2 - t1)
    y_py_sort.append(t2 - t1)


# plt.plot(x_values, y_bubble_sort, label="bubble_sort")
# plt.plot(x_values, y_selection_sort, label="selection_sort")
# plt.plot(x_values, y_insertion_sort_slow, label="insertion_sort (slow)")
# plt.plot(x_values, y_insertion_sort, label="insertion_sort")
plt.plot(x_values, y_quick_sort, label="quick_sort")
plt.plot(x_values, y_py_sort, label="pythons timsort")
plt.xlabel('length of list')
plt.ylabel('time')
plt.legend(loc='upper left')
#plt.ylim(0, 11)
plt.grid()
plt.show()
