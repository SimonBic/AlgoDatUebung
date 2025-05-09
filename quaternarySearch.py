def quaternarySearchWithIndex (Array, el, indexLeft):
    if len(Array) == 0:
        return False
    elif len(Array) == 1:
        if Array[0] == el:
            return indexLeft
        else:
            return False
    else:
        middelOfArray = (len(Array) // 2)
        quarterOfArray = middelOfArray // 2
        thirdQuarterOfArray = middelOfArray + quarterOfArray
        if(Array[middelOfArray] == el):
            return indexLeft + middelOfArray
        elif (Array[middelOfArray] > el):
            if (Array[quarterOfArray] > el):
                ArrayMod = Array[0:quarterOfArray]
                indexLeftMod = indexLeft
                return quaternarySearchWithIndex(ArrayMod, el, indexLeftMod)
            else:
                ArrayMod = Array[quarterOfArray:middelOfArray]
                indexLeftMod = quarterOfArray + indexLeft
                return quaternarySearchWithIndex(ArrayMod, el, indexLeftMod)
        else:
            if(Array[thirdQuarterOfArray] > el):
                ArrayMod = Array[(middelOfArray + 1): thirdQuarterOfArray]
                indexLeftMod = indexLeft + middelOfArray + 1
                return quaternarySearchWithIndex(ArrayMod, el, indexLeftMod)
            else:
                ArrayMod = Array[(thirdQuarterOfArray + 1): len(Array)]
                indexLeftMod = indexLeft + thirdQuarterOfArray + 1
                return quaternarySearchWithIndex(ArrayMod, el, indexLeftMod)


testArray = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,20,21,22,25,30]
indexSearch = quaternarySearchWithIndex(testArray, 11, 0)

print(indexSearch)