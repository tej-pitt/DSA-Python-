

""" Program: Bubble sort 
    Date: 13/2/2017  """ 

import random 

def bubble_sort(items):
    """ Bubble sort implementation"""
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] >= items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] #swapped
                
#Test the algorithm with random items                
rand_items= [random.randint(-50,100)for c in range(32)]

print 'Before: ', rand_items

bubble_sort(rand_items)

print 'After: ', rand_items

                


