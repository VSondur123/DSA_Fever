nums=[1,0,0,4]
pd=1
countz=nums.count(0)
flag=0
for i in nums:
    if i==0:
        flag=1
        pass
    else:
        pd*=i
l=[]
for i in nums:
    if flag==0: #if no zero 
        l.append(int(pd/i))
    elif i!=0 and flag==1: #if 1 zero or many zero but non zero element has to be zero 
        l.append(0)
    elif countz>=2: #incase there are more than 1 zero than in 0's position there should be zero example 0,0 0,0 
        l.append(0)
    else: #else incase there are 1 zero at zero's position the resultant product is placed
        l.append(pd)
print(l)