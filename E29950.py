a=input()
n=len(a)
i=0
j=0
ans=0
s=set()
while(i<n and j<n):
    if(a[j] not in s):
        s.add(a[j])
        j+=1
        ans=max(ans,j-i)
    else:
        s.remove(a[i])
        i+=1
print(ans)