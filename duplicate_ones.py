mylist = list(map(int, input("Please enter the List(with spaces) Sharvari: ").split()))
print(mylist)

def sharvari(mylist):
    ones, max_ones = 0, 0
    for i in mylist:
        if i == 1:
            ones+= 1
            max_ones = max(ones, max_ones)
        else:
            ones = 0
    return max_ones

print(sharvari(mylist))
