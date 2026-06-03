x=input()
n=len(x)
while(True):
    try:
        s=input()
        t=[]
        i=0#s
        j=0#x
        if(len(s)!=n):
            print("NO")
            continue
        while(j<n):
            if(len(t)>0 and s[i]==t[-1]):
                t.pop()
                i+=1
            else:
                t.append(x[j])
                j+=1
        while(i<n):
            if(len(t)>0 and s[i]==t[-1]):
                t.pop()
                i+=1
            else:
                break
        if(len(t)==0):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break