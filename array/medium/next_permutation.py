def reverse(nums, start):
    i, j = start, len(nums) - 1
    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

nums=[4,2,1,3]
i = len(nums) - 2
l=len(nums)
while i >= 0 and nums[i + 1] <= nums[i]:  #finding element position in decreasing order for example 1 2 3 7 3 2 1 i will be 3 position hint check 1<2 go back 2<3 go back 3<7 go back 7<3 stop
    i -= 1
if i >= 0:
    j = len(nums) - 1
    while nums[j] <= nums[i]: #finding element position greater than element at ith position
            j -= 1
    
    swap(nums, i, j)
reverse(nums,i+1)
print(nums)