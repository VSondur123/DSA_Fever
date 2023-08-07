l=list(map(int,input().split()))
n=len(l)
for i in range(0,len(l)//2):
    l[i],l[n-i-1]=l[n-i-1],l[i] 
print(l)