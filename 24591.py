n=int(input())
val={"+":1,"-":1,"*":2,"/":2}
for _ in range(n):
    s=input()
    num=""
    ans=[]
    sign=[]
    for i in s:
        if(i.isdigit() or i=='.'):
            num+=i
        else:
            if(num!=""):
                ans.append(num)
                num=""
            if(i=="("):
                sign.append(i)
            elif(i==')'):
                while(sign and sign[-1]!="("):
                    temp=sign[-1]
                    sign.pop()
                    ans.append(temp)
                sign.pop()
            elif(i in "+-*/"):
                while(sign and sign[-1] in "+-*/" and val[sign[-1]]>=val[i]):
                    temp=sign[-1]
                    sign.pop()
                    ans.append(temp)
                sign.append(i)
    if(num!=""):
        ans.append(num)
    while(sign):
        ans.append(sign.pop())
    print(" ".join(ans))