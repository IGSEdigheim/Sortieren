import random
from time import *
import sys
import matplotlib.pyplot as plt
import Sortierverfahren.BubbleSort as bs
import Sortierverfahren.SelectionSort as ss
import Sortierverfahren.InsertionSort as ins
import Sortierverfahren.QuickSort as qs


# 1. Bitte wählen Sie hier, wie lang die Liste für die Tests maximal werden soll.

maximum = 1001
sys.setrecursionlimit(maximum+2)


# 2. Bitte wählen Sie welche Daten Sie sortieren möchten, indem Sie die entsprechenden Zeilen auskommentieren

# Erzeuge zufällige Liste von Zahlen
liste = random.sample(range(maximum), maximum)
plt.title('Zufällige Zahlenliste ohne Wiederholungen')

# Erzeuge umgekehrt sortierte Liste von Zahlen
# liste = list(range(maximum,0,-1))
# plt.title('Umgekehrt sortierte Zahlenliste')

# Lade Passwort-Datei zum sortieren
# with open('Passwords/10-kilo-pw.txt', 'rt', encoding="ISO-8859-1") as f:  #'10-million-pw.txt'
#     liste = f.read().splitlines()
# plt.title('Zufällige Zeichenfolgen')


# 3. Bitte wählen Sie die Sortierverfahren aus, die Sie gegeneinander antreten lassen möchten.

measure = {"Bubble_sort": True,
           "Selection_sort": True,
           "Insertion_sort_slow": True,
           "Insertion_sort": True,
           "Quick_sort": False,
           "Tim_sort": False}

x_values = []
y_bubble_sort = []
y_selection_sort = []
y_insertion_sort_slow = []
y_insertion_sort = []
y_quick_sort = []
y_py_sort = []

for length in range (0, maximum, maximum // 20):
    x_values.append(length)

    if measure["Bubble_sort"]:
        t1 = time()
        print("bubble_sort,         ", end='')
        bs.bubble_sort(liste[:length])
        t2 = time()
        print(length, ",", t2 - t1)
        y_bubble_sort.append(t2 - t1)

    if measure["Selection_sort"]:
        t1 = time()
        print("selection_sort,      ", end='')
        ss.selection_sort(liste[:length])
        t2 = time()
        print(length, ",", t2 - t1)
        y_selection_sort.append(t2 - t1)

    if measure["Insertion_sort_slow"]:
        t1 = time()
        print("insertion_sort_slow, ", end='')
        ins.insertion_sort_slow(liste[:length])
        t2 = time()
        print(length, ",", t2 - t1)
        y_insertion_sort_slow.append(t2 - t1)

    if measure["Insertion_sort"]:
        t1 = time()
        print("insertion_sort,      ", end='')
        ins.insertion_sort(liste[:length])
        t2 = time()
        print(length, ",", t2 - t1)
        y_insertion_sort.append(t2 - t1)

    if measure["Quick_sort"]:
        t1 = time()
        print("quick_sort,          ", end='')
        qs.quick_sort(liste[:length], 0, len(liste[0:length]) - 1)
        t2 = time()
        print(length, ",", t2 - t1)
        y_quick_sort.append(t2 - t1)

    if measure["Tim_sort"]:
        t1 = time()
        print("pythons timsort,     ", end='')
        liste[:length].sort()
        t2 = time()
        print(length, ",", t2 - t1)
        y_py_sort.append(t2 - t1)


if measure["Bubble_sort"]:
    plt.plot(x_values, y_bubble_sort, label="bubble_sort")
if measure["Selection_sort"]:
    plt.plot(x_values, y_selection_sort, label="selection_sort")
if measure["Insertion_sort_slow"]:
    plt.plot(x_values, y_insertion_sort_slow, label="insertion_sort (slow)")
if measure["Insertion_sort"]:
    plt.plot(x_values, y_insertion_sort, label="insertion_sort")
if measure["Quick_sort"]:
    plt.plot(x_values, y_quick_sort, label="quick_sort")
if measure["Tim_sort"]:
    plt.plot(x_values, y_py_sort, label="pythons timsort")

plt.xlabel('length of list')
plt.ylabel('time')
plt.legend(loc='upper left')
plt.grid()
plt.show()
