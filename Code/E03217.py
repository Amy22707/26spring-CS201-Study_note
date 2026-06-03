from collections import defaultdict
n,t=map(int,input().split())
s=list(map(int,input().split()))
d=defaultdict(int)
for i in range(n):
    if(s[i] in d):
        continue
    else:
        d[s[i]]=i+1
ans=(n,n)
for i in range(n):
    if(t-s[i] in d and ans>(d[t-s[i]],i+1) and ((i+1)!=d[t-s[i]])):
        ans=(d[t-s[i]],i+1)
print(ans[0],ans[1])