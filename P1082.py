x=0
y=0
def exgcd(a,b):#ax+by=gcd(a,b)
    global x,y
    if(b==0):
        x=1
        y=0
        return
    exgcd(b,a%b)
    x,y=y,x-(a//b)*y
a,b=map(int,input().split())
exgcd(a,b)
print((x%b+b)%b)