#Pass by values (Immutable objects e.g string, tuple, float, integer)
'''When pass to function, a copy of the object is created and assigned to local value of the function.
Any changes made inside function will not reflected to the outside of the function'''
def passval(x):
    x = x+1
    print("Inside value of x is:", x)

x = 5
passval(x)
print("Outside value of x is:", x)

#Pass by reference (Mutable objects e.g list, dictionary)
'''A referance to actual object is passed by function, changes inside will affected to original object.'''
def passref(lst):
    lst.append(4)
    print("Inside list:", lst)

lst=[1,2,3]
passref(lst)
print("Outside list", lst)