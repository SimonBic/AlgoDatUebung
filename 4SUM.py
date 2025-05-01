testArray1 = [3,2,1,0]
testArray2 = [5,7,9]
testArray3 = [1]
testArray4 = [4,6]

def quicksort(list):

    if (len(list) <= 1):
        return list

    listSmaller = []
    listBigger = []
    pivot = list[0]

    for i in (list):
        if (i < pivot):
            listSmaller.append(i)
        elif (i > pivot):
            listBigger.append(i)

    listSmaller.append(pivot)
    return quicksort(listSmaller) + quicksort(listBigger)

def binarySearch (Array, el):
    if len(Array) == 0:
        return False
    elif len(Array) == 1:
        if Array[0] == el:
            return True
        else:
            return False
    else:
        middelOfArray = (len(Array) // 2)
        if(Array[middelOfArray] == el):
            return True
        elif (Array[middelOfArray] >= el):
            ArrayMod = Array[0:middelOfArray]
            return binarySearch(ArrayMod, el)
        else:
            ArrayMod = Array[(middelOfArray + 1): len(Array)]
            return binarySearch(ArrayMod, el)

def FourSUM (Array1, Array2, Array3, Array4, t):
    Array1PlusArray2 = []
    for el1 in Array1:
        for el2 in Array2:
            elNew = el1 + el2
            Array1PlusArray2.append(elNew)
    Array3PlusArray4 = []
    for el3 in Array3:
        for el4 in Array4:
            elNew = el3 + el4
            Array3PlusArray4.append(elNew)

    Array12 = quicksort(Array1PlusArray2)
    Array34 = quicksort(Array3PlusArray4)

    finalAnswer = False
    for el in Array12:
        answer = binarySearch(Array34, (t - el))
        if answer == True:
            finalAnswer = True
            break

    return finalAnswer

tIn4Sum = FourSUM(testArray1, testArray2, testArray3, testArray4, 8)
print(tIn4Sum)

#Begründung und Laufzeit:
"""
n := maximale Anzahl an Elementen in einer der Listen
S(n) := Zeit zum Sortieren einer Liste
log := Zweiter Logarithmus (Notationsprobleme hier im Compiler)

Zu Beginn des Algorithmus werden mit Hilfe einer einfach verschachtelten Schleife alle Elemente von dem ersten Array und 
dem zweiten Array kombiniert in eine Liste, sodass jede mögliche (Paar)Summe aus jedem Element von Array1 und Array2 in 
der neuen Liste vorhanden ist. Dann das Gleiche mit Array3 und Array4. 
    ->  Dieser Schritt benötigt 2 * O(n^2) Schritte, da jedes Element aus der ersten Liste mit jedem Element aus der 
        zweiten Liste kombiniert wird, also n * n = n^2. Das ganze zweimal, also 2 * O(n^2) < (2 * O(n^2 * log n)), da
        log n ab n >=2 echt positiv ist
        
Dann werden beide neuen Liste mit Hilfe eines recycelten quicksort Algorithmus von mir aus dem erstem Semester sortiert,
ich vermute, dass ich deswegen hier nicht weiter darauf eingehen muss.
    ->  2 * S(n)
    
Zum Schluss wird der binary-Search-Algorithmus aus Aufgabe 1a) wiederverwendet, nur diesmal ohne Index, da dieser hier 
keinen Nutzen hätte. Es wird überprüft mit Hilfe einer Schleife, ob mindestens eine Paarsumme aus Array1 und Array2 
addiert mit einer Paarsumme aus Array3 und Array4 das gewünschte Ergebnis ergibt. Dieses Ergebnis wird dann aus der 
Methode FourSUM zurückgegeben. 
    ->  Für jedes Element von der im ersten Schritt neu erstellten Liste, welche die Größe n^2 hat, wird der binarySearch
        Algorithmus verwendet mit einer Laufzeit von O(log n^2) = O(2 log n) = 2 * O(log n). Beide Schritte kombiniert
        also 2 * O(n^2 * log n)
        
Alle Laufzeiten addiert:
    2 * O(n^2) + 2 * S(n) + 2 * O(n^2 * log n) = 
    4 * O(n^2 * log n + 0 + 0,5 * S(n)
    -> liegt in der gewünschten Laufzeit
    
    (Ineffizenz durch Python durch Listensplitting wie in 1a) erklärt wird nicht beachtet)
"""