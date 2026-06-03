while(True):
    n=int(input())
    if(n==0):
        break
    a=list(map(int,input().split()))
    cycles=[]
    for i in range(n):
        temp=[]
        cur=-1
        while(cur!=i):
            if(cur==-1):
                cur=i
            temp.append(cur)
            cur=a[cur]-1
        cycles.append(temp)
    while(True):
        s=input()
        if(s=='0'):
            break
        idx=s.find(" ")
        k=int(s[:idx])
        t=s[idx+1:]
        t=t+" "*(n-len(t))
        res=["**"]*n
        for i in range(n):
            res[cycles[i][k%len(cycles[i])]]=t[i]
        ans=""
        for i in range(n):
            if(res[i]!="**"):
                ans+=res[i]
        print(ans)
    print()