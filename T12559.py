from functools import cmp_to_key
def cmp_max(x,y):
    if(x+y>y+x):
        return -1
    elif(x+y==y+x):
        return 0
    else:
        return 1
def cmp_min(x,y):
    if(x+y>y+x):
        return 1
    elif(x+y==y+x):
        return 0
    else:
        return -1
n=int(input())
a=list(input().split())
maxa=sorted(a,key=cmp_to_key(cmp_max))
mina=sorted(a,key=cmp_to_key(cmp_min))
print("".join(maxa),"".join(mina))