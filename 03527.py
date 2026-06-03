from collections import Counter
def check(x,y,z):
    if(x+1==y and y+1==z):
        return True
    if(x==y and y==z):
        return True
def HU(s):
    n=len(s)
    i=0
    while(i<n-2):
        if(not check(s[i],s[i+1],s[i+2])):
            return False
        i+=3
    return True
while(True):
    s=input()
    if(s=='0'):
        break
    s=list(map(int,s.split()))
    n=len(s)
    if(n%3!=2):
        print("XIANGGONG")
        continue
    s.sort()
    a=Counter(s)
    flag=0
    for i in range(1,10):
        if(a[i]>=2):
            t=s.copy()
            t.remove(i)
            t.remove(i)
            if(HU(t)):
                print("HU")
                flag=1
                break
    if(flag==0):
        print("BUHU")
