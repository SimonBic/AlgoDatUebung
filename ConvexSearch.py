def binarySearchConvexMinimumIndex (Array, indexLeft):
    if len(Array) == 2:
        if(Array[0] <= Array[1]):
            return indexLeft
        else:
            return indexLeft + 1
    elif (len(Array) == 1):
        return indexLeft
    else:
        middelOfArray = (len(Array) // 2)
        if(Array[middelOfArray] <= Array[middelOfArray + 1]):
            ArrayMod = Array[0:middelOfArray + 1]
            indexLeftMod = indexLeft
            return binarySearchConvexMinimumIndex(ArrayMod,  indexLeftMod)
        else:
            ArrayMod = Array[(middelOfArray + 1): len(Array)]
            indexLeftMod = indexLeft + middelOfArray + 1
            return binarySearchConvexMinimumIndex(ArrayMod, indexLeftMod)

testArray = [9,6,5,4,3,2,3,4,5,6,7]

answer = binarySearchConvexMinimumIndex(testArray, 0)

print(answer)

#Begründung und Laufzeit:
"""
Der Algorithmus ist von der Logik ähnlich zu dem von Aufgabe 1a), mit kleinen, folgenden Abänderungen:

    -   Falls das Array 2 oder weniger Elemente durch Zerschneidung besitzt werden alle Elemente, falls nötig verglichen
        und der Index des kleineren zurückgegeben. (Base Cases)
    -   Falls das Array mehr Elemente besitzt wird der mittlere Wert mit dem Wert danach verglichen, und falls erste
        Wert kleiner ist, muss das gesuchte Minimum links von dem untersuchten Wert liegen (oder der untersuchte Wert 
        sein)(vergl. dazu linke Skizze), also wird das Array dort geteilt und die Funktion rekursiv aufgerufen, bis ein 
        Basecase auftritt. Konträr verhält sich der Algorithmus, falls der erste Wert größer als der Zweite ist. (rechte 
        Skizze).
    
Die Laufzeit verhält sich wie beim Algorithmus bei Aufgabe 1a)SS
"""