'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
https://www.geeksforgeeks.org/array-rotation/
'''


def array_rotate(mylist, d, n):
    temp = [None]*d   #declaring size with None is v important, code wouldnt work otherwise
    for i in range(d):
        temp[i] = mylist[i]
    mylist = mylist+ temp


    return mylist[d:]






mylist = list(map(int, input("Enter list:").split()))
n = len(mylist)
d = int(input("how many elements you want to rotate: "))

print(array_rotate(mylist,d,n))