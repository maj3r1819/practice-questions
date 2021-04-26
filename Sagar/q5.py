'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
https://www.geeksforgeeks.org/array-rotation/
'''


def array_rotate(mylist, d, n):
    for i in range(d):
        mylist.append(mylist[i])
    for i in range(d):
        mylist.pop(0)

    return mylist






mylist = list(map(int, input("Enter list:").split()))
n = len(mylist)
d = int(input("how many elements you want to rotate: "))

print(array_rotate(mylist,d,n))