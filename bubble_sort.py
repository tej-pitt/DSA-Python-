""" Author: Tejas Pitkar
    Script: Bubble sort algo """

def bubbleSort(alist):
    n=len(alist)
    while n>1:
        i=1
        while i<n:
            if alist[i]<alist[i-1]:
                temp=alist[i]
                alist[i]=alist[i-1]
                alist[i-1]=temp
            i += 1
        n -= 1
        
alist = [54,32,24,66,12,25,30,49,5]
bubbleSort(alist)
print (alist)


                


