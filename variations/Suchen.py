def lineare_suche1(suchwert, liste):
    n = len(liste)
    i = 0
    erg = -1
    while i < n and erg == -1:
        if suchwert == liste[i]:
            erg = i
        i += 1
    return erg

def lineare_suche2(suchwert, liste):
    n = len(liste)
    i = 0
    while i < n:
        if suchwert == liste[i]:
            return i
        i += 1
    return -1

def binary_search(suchwert, liste):
    links = 0
    rechts = len(liste)-1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if suchwert == liste[mitte]:
            return mitte
        elif suchwert < liste[mitte]:
            rechts = mitte-1
        else:
            links = mitte+1
    return -1

zahlen = [3,7,19,21,22,24,28,30,31,36,40,42,48,49,52,53,60,70,72,80]
print(lineare_suche1(72,zahlen))
print(binary_search(72,zahlen))


#n = Länge von A
#i = 0
#erg = -1
#e = Eingabe
#solange i < n und erg = -1
#wiederhole
#	wenn e = A[i] dann
#		erg = i
#	ende wenn
#	i = i+1
#ende solange
#Rückgabe von erg
