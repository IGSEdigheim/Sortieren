def suchen(name, liste):
    n = len(liste)
    erg = -1
    i = 0
    while erg == -1 and i < n:
        if name == liste[i]:
            erg = i
        i += 1
    return erg

zahlen = [1,2,5,8,11,13,22,42]
print(suchen(42,zahlen))


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
