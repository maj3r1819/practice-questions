mylist = list(map(int, input("Please enter the List(with spaces) Sharvari: ").split()))
print(mylist)

def sharvari(mylist):
    newlist =[]
    for i in range(len(mylist)):
        num = mylist[i]
        count,max_count = 0,0
        while num!=0:
            num = num//10
            count+=1
        max_count = max(max_count, count)
        newlist.append(max_count)
    index = newlist.index(max(newlist))

    return mylist[index]

print(sharvari(mylist))