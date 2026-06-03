def gcd(a,b):
    a=abs(a)
    b=abs(b)
    if(a<b):
        a,b=b,a
    while(a%b!=0):
        c=a%b
        a=b
        b=c
    return b
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()
    def simplify(self):
        a=self.numerator
        b=self.denominator
        if(a==0):
            self.numerator=0
            self.denominator=1
            return
        c=gcd(a,b)
        self.numerator=a//c
        self.denominator=b//c
    def __add__(self,other):
        a,b,c,d=self.numerator,self.denominator,other.numerator,other.denominator
        e=a*d+b*c
        f=b*d
        return Fraction(e,f)
    def __str__(self):
        a=self.numerator
        b=self.denominator
        if(b==1):
            return f"{a}"
        return f"{a}/{b}"
a,b,c,d=map(int,input().split())
x=Fraction(a,b)
y=Fraction(c,d)
print(x+y)