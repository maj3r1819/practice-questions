nums = [4, 1, 2, 1, 2]
count = 0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print(nums[i])
            count+=1
print(count)