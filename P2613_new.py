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
x=1
if(new_b==0):
    print("Angry!")
    sys.exit(0)
i=mod-2
t=new_b
while(i):
    if(i&1):
        x=x*t%mod
    t=t*t%mod
    i>>=1
print((x*new_a)%mod)