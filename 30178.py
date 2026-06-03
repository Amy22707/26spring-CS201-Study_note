def lowbit(x):
    return x&(-x)
class BIT:
    def __init__(self,n):
        self.n=n
        self.tree=[0]*(n+1)
    def update(self,idx,x):
        while(idx<=self.n):
            self.tree[idx]+=x
            idx+=lowbit(idx)
    def query(self,idx):
        ans=0
        while(idx>0):
            ans+=self.tree[idx]
            idx-=lowbit(idx)
        return ans
n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    if(0 in t):
        tmp=i
        t.remove(0)
    a.extend(t)
m=n*n-1
b=BIT(m)
ans=0
for i in range(m-1,-1,-1):
    ans+=b.query(a[i]-1)
    b.update(a[i],1)
if(n%2==0):
    ans+=(n-tmp-1)
    if(ans%2==0):
        print("yes")
    else:
        print("no")
else:
    if(ans%2==0):
        print("yes")
    else:
        print("no")