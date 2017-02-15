""" Program: Quick_sort 
    Date: 15/2/2017 """
    
import random 

def quick_sort(items):
    #implement quick sort algorithm
    if len(items) > 1:
        pivot_ind = len(items)/2 #divide into 2 lists with pivot 
        smaller = []
        larger = []
        
        for i, val in enumerate(items): #enumerate gives reliable index to iterable items.
            if i!= pivot_ind:
                if val < items[pivot_ind]: #if valuation less than pivot 
                    smaller.append(val)
                else:
                    larger.append(val) #if valuation greater than pivot 
            
        quick_sort(smaller) #recursive function on 2 lists 
        quick_sort(larger)
        items[:]= smaller + [items[pivot_ind]] + larger #final merging of all lists 


#test the algo with random numbers        
rand_items= [random.randint(-50,100)for c in range(32)]

print 'Before: ', rand_items

quick_sort(rand_items)

print 'After: ', rand_items       
