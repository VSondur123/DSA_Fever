mx=0
sm=0
cnt=0
nums = [-2,-6,-1]
for i in nums:
    #Condition for case if all numbers are negative
    if i<0:
        cnt+=1
    #Cumulative sum till sum < 0, then initialise sum = 0
    sm += i
    if sm < 0:
        sm = 0

    mx = max(sm,mx)

if cnt == len(nums):
    print(max(nums))
else:
    print(mx)