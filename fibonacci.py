""" Author: Tejas Pitkar
    Program: Fibonacci numbers in loop """

from counter import Counter
def fib(n,counter):
    """ Count the number of iterations in the fibonacci 
    function """
    sum=1 
    first= 1
    second=1
    count=3
    while count<=n:
        counter.increment()
        sum= first + second
        first = second 
        second = sum 
        count += 1
    return sum 
    

problemSize = 2
print ("%12s%15s" %("Problem size", "Calls"))
for count in range(5):
    counter= Counter()
    #the start of the algo
    fib(problemSize, counter)
    #the end of the algo 
    
    print("%12d %15s" %(problemSize,counter))
    problemSize *= 2  