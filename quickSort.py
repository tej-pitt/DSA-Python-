""" Program: Quick sort algorithm
    Author: Tejas Pitkar """
    
def quicksort(lyst):
    quicksortHelper(lyst,0,len(lyst)-1)
    
def quicksortHelper(lyst,left,right):
    if left < right:
        pivotLocation= partition(lyst,left,right)
        quicksortHelper(lyst,left, pivotLocation -1)
        quicksortHelper(lyst,pivotLocation +1 , right)
        

def partition(lyst,left,right):
    #Find the pivot and exchange with the last item 
    middle= (left + right)//2
    pivot= lyst[middle]
    lyst[middle]=lyst[right]
    lyst[right]= pivot 
    #Set boundary point to first position
    boundary= left 
    #Move items less than pivot to the left 
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst,index,boundary)
            boundary += 1
    # Exchange the pivot item and boundary item
    swap(lyst,right,boundary)
    return boundary
    #Customary swap function to exchange items 
def swap(lyst,i,j):
    #Exchanges items at locations i and j
    temp = lyst[i]
    lyst[i]= lyst[j]
    lyst[j]= temp
    
import random

def main(size=30, sort=quicksort):
    lyst= []
    for count in range(size):
        lyst.append(random.randint(1,size+1))
    print (lyst)
    sort (lyst)
    print (lyst)

if __name__ == "__main__":
     main()
     
