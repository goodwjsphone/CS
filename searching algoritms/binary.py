def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList) -1
    while first <= last and found == False:
        midpoint = (first + last) / 2
        if aList[midpoint] == itemSought:
            found = True
            index == midpoint
        else:
            if aList[midpoint] < itemSought:
                first = midpoint
            else:
                last = midpoint

    print (index)
list = [1,2,3,4,5,6,7,8,9,10]
binarySearch(list, 4)

