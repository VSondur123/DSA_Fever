m=int(input())
l=list(map(int,input().split()))
n=len(l)
l.sort()
print(l)
s=max(l)+min(l)
for i in range(0,len(l)-m+1):
    s=min(s,l[i+m-1]-l[i])
print(s)
