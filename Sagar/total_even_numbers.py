"""
4)Given an array with many numbers, display as output the total number
 of numbers having even number of digits
 """
mylist = list(map(int, input("Please enter the List(with spaces) Sharvari: ").split()))
print(mylist)

def sharvari(mylist):
    count,count1 = 0,0
    for i in mylist:
        while i!=0:
            i = i//10
            count+=1
        if count%2 ==0:
            count1+=1

    return count1

print(sharvari(mylist))


