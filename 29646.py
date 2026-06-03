n=int(input())
for _ in range(n):
    bad,good=map(int,input().split())
    res=0
    while(bad>0):
        res+=1
        bad-=good
        if(bad<=0):
            break
        bad<<=1
        if(bad>1000000):
            bad=1000000
        good=int(1.05*good)
    print(res)