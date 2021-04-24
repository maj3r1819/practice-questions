num = int(input("please enter the number  sharvari :"))

def sharvari(num):
    count = 0
    while num!=0:
        num = num//10
        count+=1

    return count

print(sharvari(num))