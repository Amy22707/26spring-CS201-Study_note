n=int(input())
a=[0]+list(map(int,input().split()))
s=[]
is_max=1
is_min=1
def dfs(x,path):
    global is_max,is_min
    if(2*x>n):
        s.append(path)
        return
    if(2*x+1<=n):
        if(a[2*x+1]>a[x]):
            is_max=0
        if(a[2*x+1]<a[x]):
            is_min=0
        dfs(2*x+1,path+[a[2*x+1]])
    if(2*x<=n):
        if(a[2*x]>a[x]):
            is_max=0
        if(a[2*x]<a[x]):
            is_min=0
        dfs(2*x,path+[a[2*x]])
dfs(1,[a[1]])
for i in range(len(s)):
    print(*s[i])
if(is_max):
    print("Max Heap")
elif(is_min):
    print("Min Heap")
else:
    print("Not Heap")