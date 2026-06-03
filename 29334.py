a=input()
n=len(a)
ans=0
for i in range(n):
    ans*=26
    ans+=ord(a[i])-ord('A')+1
print(ans)