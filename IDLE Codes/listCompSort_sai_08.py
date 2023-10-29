'''
    Author: Saikumar Srinivas
    Filename: listCompSort_sai_08.py
    Purpose: Simple List Comprehension & Sorting Template
    Complete the list comprehension exercises here
    Any functions you write must also have
    (1) a docstring that describes the input parameters
        and the value returned
    (2) at least two significant tests that verify the function
'''
###### 1. List comprehension analysis
### Code
def linc(a,b=2):
    '''
    Returns a new list with the values incremented by the value of 'b'.
    
    Parameters:
    a (list): A list of elements.
    b (int): The value to increment the elements in the list (default is 2).
    
    Returns:
    list: A new list with incremented values.
    '''
    return [i + b for i in a if isinstance(i, int)]
x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x)
print(y)
print(z)

###### 2. the listInc() function
def listInc(a):
    '''
    Increments the integers in a list by 1.
    
    Parameters:
    a (list): A list of elements.
    
    Returns:
    list: A new list with incremented integer values.
    '''
    return [i + 1 for i in a if isinstance(i, int)]
### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
# listInc should not only increment the ints but also
# ignore the floats, strings, etc.
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('\nlistInc is OK\n')

###### 3. the listOut() function
def listOut(a):
    '''
    Returns a single string where each item from the input list is printed on a separate line.

    Parameters:
    a (list): A list of items.

    Returns:
    str: A single string where each item is printed on a separate line.
    '''
    return '\n'.join(str(item) for item in a)
### listOut() tests
listOut([7,2,'OK',8])
print(listOut([7,2,'OK',8]))
print()
listOut([[1,2],2.0,'$',8])
print(listOut([[1,2],2.0,'$',8]))
print()

###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0, a.pop())
print(a,b)
### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
b.append(a.pop(0))
print(a,b,'\n')

###### 5a. the rotateForward() function
def rotateForward(a):
    '''
    Rotates the elements of the list one position forward.
    
    Parameters:
    a (list): A list of elements.
    
    Returns:
    list: A new list with the elements rotated one position forward.
    '''
    return a[-1:] + a[:-1]
### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')

###### 5b. the rotateForward() function
def rotateBackward(a):
    '''
    Rotates the elements of the list one position backward.
    
    Parameters:
    a (list): A list of elements.
    
    Returns:
    list: A new list with the elements rotated one position backward.
    '''
    return a[1:] + a[:1]
### rotateBackward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1], 'rotateBackward failed'
print('rotateBackward ok\n')

###### 6. Analysis of iSort()
def iSort(x,n=2):
    '''
    Sorts the list based on the nth element in each sublist.
    
    Parameters:
    x (list): A list of sublists.
    n (int): The index to use for sorting (default is 2).
    
    Returns:
    list: A new list sorted based on the nth element in each sublist.
    '''
    return sorted(x, key=lambda a: a[n - 1])
x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()

###### 7. Length sorting
z = ['bzz','z','cz','azzz']
z.sort(key=len)
print(z,'\n')

###### 8. the backSort() function
def backSort(a):
    '''
    Sorts a list in descending order.
    
    Parameters:
    a (list): A list of elements.
    
    Returns:
    list: A new list sorted based on the last letter in each string.
    '''
    return sorted(a, key=lambda x: x[-1], reverse=False)
### backSort() tests
assert backSort(['red', 'yellow', 'blue', 'green', 'black']) == ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')
