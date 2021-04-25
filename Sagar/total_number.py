"""
2)Find the number of digits in any number 'n'  eg: n=777--->op=3, n=89--->op=2
"""
num = int(input("please enter the number  sharvari :"))

def sharvari(num):
    count = 0
    while num!=0:
        num = num//10
        count+=1

    return count

print(sharvari(num))