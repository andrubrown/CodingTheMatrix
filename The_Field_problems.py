# version code 75eb0ae74c69
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Python Comprehensions: Filtering
def myFilter(L, num):
    '''
    Input:
      -L: a list of numbers
      -num: a positive integer
    Output:
      -a list of numbers not containing a multiple of num
    Examples:
      >>> myFilter([1,2,4,5,7],2)
      [1, 5, 7]
      >>> myFilter([10,15,20,25],10)
      [15, 25]
    '''
    return [x for x in L if x % num != 0]



## 2: (Problem 2) Python Comprehensions: Lists of Lists

def my_lists(L):
    '''
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    return [list(range(1,x+1)) for x in L]



## 3: (Problem 3) Python Comprehensions: Function Composition
def myFunctionComposition(f, g):
    '''
    Input:
      -f: a function represented as a dictionary such that g of f exists
      -g: a function represented as a dictionary such that g of f exists
    Output:
      -a dictionary that represents a function g of f
    Examples:
      >>> f = {0:'a',1:'b'}
      >>> g = {'a':'apple','b':'banana'}
      >>> myFunctionComposition(f,g) == {0:'apple',1:'banana'}
      True

      >>> a = {'x':24,'y':25}
      >>> b = {24:'twentyfour',25:'twentyfive'}
      >>> myFunctionComposition(a,b) == {'x':'twentyfour','y':'twentyfive'}
      True
    '''
    return { k:g[v] for k,v in f.items() }



## 4: (Problem 4) Summing numbers in a list
def mySum(L):
    '''
    Input:
      a list L of numbers
    Output:
      sum of the numbers in L
Be sure your procedure works for the empty list.
    Examples:
      >>> mySum([1,2,3,4])
      10
      >>> mySum([3,5,10])
      18
    '''
    current = 0
    for x in L:
        current += x
    return current



## 5: (Problem 5) Multiplying numbers in a list
def myProduct(L):
    '''
    Input:
      -L: a list of numbers
    Output:
      -the product of the numbers in L
Be sure your procedure works for the empty list.
    Examples:
      >>> myProduct([1,3,5])
      15
      >>> myProduct([-3,2,4])
      -24
    '''
    current = 1
    for x in L:
      current *= x
    return current



## 6: (Problem 6) Minimum of a list
def myMin(L):
    '''
    Input:
      a list L of numbers
    Output:
      the minimum number in L
Be sure your procedure works for the empty list.
Hint: The value of the Python expression float('infinity') is infinity.
    Examples:
    >>> myMin([1,-100,2,3])
    -100
    >>> myMin([0,3,5,-2,-5])
    -5
    '''
    current = float('infinity')
    for x in L:
        if x < current:
            current = x
    return current



## 7: (Problem 7) Concatenation of a List
def myConcat(L):
    '''
    Input:
      -L:a list of strings
    Output:
      -the concatenation of all the strings in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myConcat(['hello','world'])
    'helloworld'
    >>> myConcat(['what','is','up'])
    'whatisup'
    '''
    current = ''
    for x in L:
        current += x
    return current



## 8: (Problem 8) Union of Sets in a List
def myUnion(L):
    '''
    Input:
      -L:a list of sets
    Output:
      -the union of all sets in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myUnion([{1,2},{2,3}])
    {1, 2, 3}
    >>> myUnion([set(),{3,5},{3,5}])
    {3, 5}
    '''
    current = set()
    for x in L:
        current |= x
    return current



## 9: (Problem 9) Complex Addition Practice
# Each answer should be a Python expression whose value is a complex number.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## 10: (Problem 10) Combining Complex Operations
#Write a procedure that evaluates ax+b for all elements in L

def transform(a, b, L):
    '''
    Input:
      -a: a number
      -b: a number
      -L: a list of numbers
    Output:
      -a list of elements where each element is ax+b where x is an element in L
    Examples:
    >>> transform(3,2,[1,2,3])
    [5, 8, 11]
    '''
    return [a*z + b for z in L]



## 11: (Problem 11) GF(2) Arithmetic
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0

