import sys
a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()
new_a=0
new_b=0
mod=19260817
for i in range(len(a)):
    new_a=(new_a*10+int(a[i]))%mod
for i in range(len(b)):
    new_b=(new_b*10+int(b[i]))%mod
x=0
y=0
if(new_b==0):
    print("Angry!")
    sys.exit(0)
def exgcd(b,m):
    global x,y
    if(m==0):
        x=1
        y=0
        return
    exgcd(m,b%m)
    x,y=y,x-(b//m)*y
exgcd(new_b,mod)
print((new_a*x)%mod)