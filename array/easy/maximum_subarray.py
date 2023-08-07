nums = [-2,1,-3,4,-1,2,1,-5,4]
mx=0
sm=0
cnt=0
l,h=0,0
x=[]
for i in range(len(nums)):
    #Condition for case if all numbers are negative
    if nums[i]<0:
        cnt+=1
    #Cumulative sum till sum < 0, then initialise sum = 0
    sm += nums[i]
    if sm < 0:
        sm = 0
        l = i+1
        x.append(0)
    if sm > mx:
        h=i
    mx = max(sm,mx)
    x.append(sm)
print(x)
print(nums[l:h+1]) #sub array 
if cnt == len(nums):
    print(max(nums))
else:
    print(mx)