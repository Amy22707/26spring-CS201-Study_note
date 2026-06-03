m=int(input())
for _ in range(m):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    ans=0
    for i in range(n):
        while(s and a[i]>a[s[-1]]):
            h=s.pop()#水槽底部
            if(s):
                ans+=(min(a[i],a[s[-1]])-a[h])*(i-s[-1]-1)
        s.append(i)
    print(ans)