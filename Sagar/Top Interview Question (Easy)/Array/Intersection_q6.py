
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
k = len(nums1)
l = len(nums2)
num3 = []
if k>=l:
    for i in range(l):
        if nums2[i] in nums1:
            num3.append(nums2[i])
            nums1.remove(nums2[i])
        else:
            continue

else:
    for i in range(k):
        if nums1[i] in nums2:
            num3.append(nums1[i])
            nums2.remove(nums2[i])

        else:
            continue
print(num3)