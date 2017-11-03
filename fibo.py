def factorial(n):
    #print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        #print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res  

print(factorial(5))


def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result
print(iterative_factorial(5))

from timeit import Timer
#from fibo import factorial

t1 = Timer("factorial(10)","from fibo import factorial")

for i in range(1,20):
    s = "factorial(" + str(i) + ")"
    t1 = Timer(s,"from fibo import factorial")
    time1 = t1.timeit(3)
    s = "iterative_factorial(" + str(i) + ")"
    t2 = Timer(s,"from fibo import iterative_factorial")
    time2 = t2.timeit(3)
    print("n=%2d, factorial: %8.6f, iterative_factorial:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib(10), fibi(10))

from timeit import Timer
#from fibo import fib

t1 = Timer("fib(10)","from fibo import fib")

for i in range(1,30):
    s = "fib(" + str(i) + ")"
    t1 = Timer(s,"from fibo import fib")
    time1 = t1.timeit(3)
    s = "fibi(" + str(i) + ")"
    t2 = Timer(s,"from fibo import fibi")
    time2 = t2.timeit(3)
    print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))

'''Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
Write a recursive Python function that returns the sum of the first n integers. 
(Hint: The function will be similiar to the factorial function!)
Write a function which implements the Pascal's triangle:
1
1    1
1    2    1
1    3    3    1
1    4    6    4    1
1    5    10    10    5    1

You find further exercises on our Python3 version of recursive functions, e.g. creating the Fibonacci numbers out of Pascal's triangle or produce the prime numbers recursively, using the Sieve of Eratosthenes.'''