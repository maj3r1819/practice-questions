"""
try this: a=[1,2,3]
b=[4,5,6]
#c=[1,4,2,5,3,6]
"""
#Only works if the ararys are of the same length


a = list(map(int, input("Enter the first list: ").split()))
b = list(map(int, input("Enter the second list: ").split()))
c = [0]*(len(a)+len(b))
i,j = 0,0
while(j<len(a)):
    c[i] = a[j]
    i+=2
    j+=1

i,j = 1,0
while(j<len(b)):
    c[i] = b[j]
    i+=2
    j+=1
print(c)