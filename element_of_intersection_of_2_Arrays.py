def binary_Search(Arr, el):
    if len(Arr) == 0:
        return False
    elif len(Arr) == 1:
        if Arr[0] == el:
            return True
        else:
            return False
    else:
        middelOfArray = (len(Arr) // 2)
        if(Arr[middelOfArray] == el):
            return True
        elif (Arr[middelOfArray] > el):
            ArrayMod = Arr[0:middelOfArray]
            return binary_Search(ArrayMod, el)
        else:
            ArrayMod = Arr[(middelOfArray + 1): len(Arr)]
            return binary_Search(ArrayMod, el)

def search_of_intersection_element(A, B):
    for elB in B:
        if (binary_Search(A, elB) == True):
            return elB
    return False

testArray1 = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,20,21,22,25,30]
testArray2 = [3,4,55,66,77]
testArray3 = [100,101]

test1 = search_of_intersection_element(testArray1, testArray2)
test2 = search_of_intersection_element(testArray1, testArray3)

print("Test 1: ", test1)
print("Test 2: ", test2)