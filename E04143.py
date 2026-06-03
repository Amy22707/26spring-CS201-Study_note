from collections import Counter
n=int(input())
a=list(map(int,input().split()))
m=int(input())
s=Counter(a)
res=[]
for c in s:
    if((c<m/2 and c!=m-c and s[c]>0 and s[m-c]>0) or (c==m/2 and s[c]>1)):
        res.append([c,m-c])
if(len(res)==0):
    print("No")
else:
    res.sort()
    print(res[0][0],res[0][1])