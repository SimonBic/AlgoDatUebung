def binarySearchWithIndex (Array, el, indexLeft):
    if len(Array) == 0:
        return False
    elif len(Array) == 1:
        if Array[0] == el:
            return indexLeft
        else:
            return False
    else:
        middelOfArray = (len(Array) // 2)
        if(Array[middelOfArray] == el):
            return indexLeft + middelOfArray
        elif (Array[middelOfArray] >= el):
            ArrayMod = Array[0:middelOfArray]
            indexLeftMod = indexLeft
            return binarySearchWithIndex(ArrayMod, el, indexLeftMod)
        else:
            ArrayMod = Array[(middelOfArray + 1): len(Array)]
            indexLeftMod = indexLeft + middelOfArray + 1
            return binarySearchWithIndex(ArrayMod, el, indexLeftMod)

testArray = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,20,21,22,25,30]

answer = binarySearchWithIndex(testArray, 20, 0)
print(answer)

#Begründung + Runtime:
"""Der Code funktioniert sehr ähnlich wie in der Vorlesung erklärt, also Folgendermaßen:


Die Methode funktioniert rekursiv (Index wird am Ende begründet):

-   2 Base-Cases, also falls das Array 0 Elemente besitzt wird False zurückgegeben, falls nur ein Element vorhanden ist,
    wird überprüft, ob es das gesuchte Element ist, falls ja, wird der Index davon zurückgegeben, falls nicht wird false 
    zurückgegeben.
-   rekursiver Fall: Falls das Array 2 oder mehr Elemente besitzt, wird zunächst das mittlere Element bestimmt und 
    überprüft, ob es zufällig das gesuchte Element ist. Falls Ja wird der Index davon zurückgegeben, falls nicht wird 
    überprüft, ob das mittlere Element kleiner oder größer ist:
        * Falls es größer ist, wird die Methode nochmal aufgerufen, und zwar nur die linke Hälfte der Liste, da dass
        gesuchte Element wenn überhaupt dort liegt, da die Liste sortiert ist.
        * Falls es kleiner ist, muss das Element wenn überhaupt im rechten Teil liegen, also wird die Methode mit der 
        rechten Hälfte aufgerufen, da das Array sortiert ist.
-   Das Ganze wird solange rekursiv wiederholt, bis entweder die Liste leer ist oder das gesuchte Element gefunden ist.

Falls das Element vorhanden ist, wird der Index angegeben, das funktioniert folgendermaßen:

    Mit jedem rekursiven Aufruf wird der ´´Linke-Index´´ übergeben, dieser ist schlicht der Index des ersten Elements
    der übergebenden Liste in Relation zur Originaliste. Deswegen wird, falls der Linke Teil der Liste weggeschnitten 
    wird, die Anzahl der weggeschnittenen Elemente addiert, damit die Relation zur Originalliste vorhanden bleibt. 
    Da der einzige wahre Fall der Basecases eine Liste mit genau einem Element ist und dieses Element das gesuchte
    Element ist, ist der Linke-Index in diesem Fall der Index des gesuchten Elements in der Originalliste und wird 
    ausgegeben. 
    Falls das mittlere Element zufällig das gesuchte Element ist wird der Index des mittleren Elements addiert und 
    ausgegeben, da dann dieser Index der Index des gesuchten Elements in der Originalliste ist.
    
    
Runtime:
    Die Logik des Codes hat eine Runtime von O(log n) (n = Anzahl der Elemente in der Liste), da bei jedem Durchlauf
    die Anzahl der Listenelement halbiert wird.
    Die tatsächliche Runtime ist aber O(n * log n), da ich Python verwendet habe, was leider bei jedem rekursiven Aufruf
    zusätzlich O(n) Zeit braucht, da ich Listensplitting verwende z.B.:  
    ArrayMod = Array[(middelOfArray + 1): len(Array)], was in Python O(n)-Zeit braucht, da alle Elemente in eine neue 
    Liste kopiert werden, in beispielsweise Java wäre die tatsächliche Runtime O(log n), da dort der Originalbereich der
    Liste verwendet wird. 
    
    Ich hoffe die Begründung ist verständlich, ich studiere absichtlich kein Deutsch ;)"""
