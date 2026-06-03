from math import gcd
def exgcd(a,b):
    if(b==0):
        return 1,0
    x,y=exgcd(b,a%b)
    return y,x-(a//b)*y
while(True):
    a,b,c,k=map(int,input().split())
    if(a*a+b*b+c*c+k*k==0):
        break
    '''
    a+cx=b(mod 2^k)
    cx=b-a(mod 2^k)
    cx+(2^k)y=b-a
    t=(b-a)/gcd(c,2^k)
    x=x0t,y=y0t
    cx0+(2^k)y0=gcd(c,2^k)

    (c/gcd)x+(2^k/gcd)y=(b-a)/gcd
    res=x+k*(2^k/gcd)
    '''
    p=1<<k
    g=gcd(c,p)
    diff=(b-a)%p
    if(diff%g!=0):
        print("FOREVER")
        continue
    #b<a:b=b+kp>a,k>(a-b)/p
    x,y=exgcd(c,p)
    p_prime=p//g
    ans=(x*diff//g)%p_prime
    print(ans)