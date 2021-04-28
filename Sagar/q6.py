'''
Q6. rotate the list
test case:
I/P : list = [1,2,3,4,5], k = 2
O/P : [4,5,1,2,3]
explanation:
first rotation: [5,1,2,3,4]
second rotation: [4,5,1,2,3]
'''



mylist = list(map(int, input().split()))
print("Original List : ", mylist )
m = int(input("Please enter by how much u want to rotate: "))
for i in range(m):
    k = mylist[len(mylist) - 1]
    for i in range((len(mylist)-1),-1, -1):
        mylist[i] = mylist[i-1]
    mylist[0] = k
print("Rotated List : ", mylist)
