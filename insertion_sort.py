""" Program: Insertion_sort 
    Date: 14/2/2017 """
    
import random 

def insertion_sort(items):
    #implementation of insertion sort algorithm 
    for i in range(1,len(items)):
        j=i 
        while j>= 0 and (items[j] < items[j-1]):
            items[j],items[j-1]= items[j-1],items[j]#swap
            j -= 1
            

#Test the algorithm with random numbers
rand_items= [random.randint(-50,100)for c in range(32)]

print 'Before: ', rand_items

insertion_sort(rand_items)#calling the above method

print 'After: ', rand_items
        
