a=list(input().split())
s1=[]
s2=[]
dic={"+":1,"-":1,"*":2,"/":2}
def cal(x,y,t):
    x=float(x)
    y=float(y)
    if(t=="+"):
        return x+y
    elif(t=="-"):
        return x-y
    elif(t=="*"):
        return x*y
    elif(t=="/"):
        return x/y
    return 0
for i in a:
    if(i.isdigit()):
        s1.append(i)
    else:
        while(s2 and dic[i]<=dic[s2[-1]]):
            t=s2.pop()
            y=s1.pop()
            x=s1.pop()
            s1.append(cal(x,y,t))
        s2.append(i)
while(s2):
    y=s1.pop()
    x=s1.pop()
    t=s2.pop()
    s1.append(cal(x,y,t))
print(f"{float(s1[-1]):.2f}")