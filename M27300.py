from collections import defaultdict
from decimal import Decimal
n=int(input())
models=defaultdict(list)
for i in range(n):
    a,b=input().split('-')
    if(b[-1]=='M'):
        c=Decimal(b[0:-1])*1000000
    elif(b[-1]=='B'):
        c=Decimal(b[0:-1])*1000000000
    models[a].append(c)
ans=dict(sorted(models.items(),key=lambda x:x[0]))
for k in ans:
    ans[k].sort()
    tmp=[]
    for i in ans[k]:
        if(i>=1000000 and i<1000000000):
            s=str(i/1000000)
            tmp.append(s+"M")
        else:
            s=str(i/1000000000)
            tmp.append(s+"B")
    print(f"{k}: {', '.join(tmp)}")