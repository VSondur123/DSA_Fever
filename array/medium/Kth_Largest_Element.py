nums=list(map(int,input().split()))
k=int(input())
nums.sort(reverse=True)
print(nums[k-1])