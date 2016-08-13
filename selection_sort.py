"""Author: Tejas Pitkar
   Script: Selection sort algo """
   


def selectionSort(lyst):
    i=0
    while i<len(lyst)-1:
        minIndex = i
        j = i+1
        while j < len(lyst):
            if lyst[j]<lyst[minIndex]:
                minIndex= j
            j += 1
        if minIndex != i:
            temp = i
            i=minIndex
            minIndex = temp 
        i += 1 
        
lyst = [1,5,3,7,9,23,2,44]
selectionSort(lyst)
print (lyst)


