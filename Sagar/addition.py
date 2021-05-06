"""
1)Can you help me with this code: to form series upto n number: 0 1 1 2 4 8...
such that the nth element will be addition of all the elements before it?...
note: this is not fibonacci series
"""


def sharvari(num):

    mylist = [0]* num    #Creates empty list of num elements

    if num == 1:        # if num is 1 just return [0]
        return mylist
    else:                   #else
        mylist[0] = 0       #declare first and second element
        mylist[1] = 1
        for i in range(2, len(mylist)):        #start from the third element
            sum = 0
            for j in range(i):          #start from 0 upto i elements
                sum = sum + mylist[j]
            mylist[i] = sum

    return mylist


print(sharvari(6))

