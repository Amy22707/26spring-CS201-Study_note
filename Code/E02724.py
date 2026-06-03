from collections import defaultdict
n=int(input())
a=defaultdict(list)
for i in range(n):
    idx,m,d=input().split()
    birth=int(m)*100+int(d)
    a[birth].append(idx)
a=dict(list(sorted(a.items(),key=lambda x:x[0])))
for i in a.keys():
    if(len(a[i])>1):
        mon=i//100
        day=i-mon*100
        print(mon,day,*a[i])