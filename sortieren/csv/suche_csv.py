import csv


def binary_search(suchwert, liste):
    links = 0
    rechts = len(liste)-1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if suchwert == liste[mitte][0]:
            return mitte
        elif suchwert < liste[mitte][0]:
            rechts = mitte-1
        else:
            links = mitte+1
    return -1


def lineare_suche(suchwert, liste):
    i = 0
    while i < len(liste):
        if suchwert == liste[i][0]:
            return i
        i += 1
    return -1


with open('adressdaten_sortiert_name.csv', 'r') as f:
  reader = csv.reader(f)
  listeDaten = list(reader)

print(binary_search("Herrmann",listeDaten))
print(lineare_suche("Herrmann",listeDaten))
