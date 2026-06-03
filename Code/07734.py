t=int(input())
for qaq in range(1,t+1):
    n,m=map(int,input().split())
    fa=[i for i in range(2*n+2)]
    siz=[1]*(2*n+2)
    def find(x):
        if(fa[x]==x):
            return x
        fa[x]=find(fa[x])
        return fa[x]
    def merge(x,y):
        fx=find(x)
        fy=find(y)
        if(fx==fy):
            return
        if(siz[fx]>siz[fy]):
            fx,fy=fy,fx
        fa[fx]=fy
        siz[fy]+=siz[fx]
    flag=0
    for i in range(m):
        x,y=map(int,input().split())
        if(flag==1):
            continue
        if(find(x)==find(y)):
            flag=1
            continue
        merge(x,y+n)
        merge(x+n,y)
    print(f"Scenario #{qaq}:")
    if(flag==0):
        print("No suspicious bugs found!")
    else:
        print("Suspicious bugs found!")
    print()