from collections import defaultdict
n=int(input())
s=input()
t=defaultdict(int)
ans=0
for i in range(len(s)-n+1):
    t[s[i:i+n]]+=1
    ans=max(ans,t[s[i:i+n]])
if(ans<=1):
    print("NO")
else:
    res=[]
    for key,val in t.items():
        if(val==ans):
            res.append(key)
    print(ans)
    print("\n".join(res))