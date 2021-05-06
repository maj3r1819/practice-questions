arr = [17,18,5,4,6,1]
arr[len(arr)-1] = -1
for i in range(len(arr)-1):
    arr[i] = max(arr[i+1:])


print(arr)
