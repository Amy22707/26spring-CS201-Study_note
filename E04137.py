t=int(input())
for _ in range(t):
    n,k=input().split()
    k=int(k)
    m=len(n)
    s=[]
    cnt=0
    for c in n:
        while(s and c<s[-1] and cnt<k):
            s.pop()
            cnt+=1
        s.append(c)
    while(cnt<k):
        s.pop()
        cnt+=1
    print("".join(s))
