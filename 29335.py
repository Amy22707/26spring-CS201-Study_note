a=input().split("/")
s=[]
n=len(a)
for i in a:
    if(i==""):
        continue
    elif(i=="."):
        continue
    elif(i==".."):
        if(s):
            s.pop()
        else:
            continue
    else:
        s.append(i)
print("/",end="")
print("/".join(s))