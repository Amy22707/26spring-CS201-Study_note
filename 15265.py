n=int(input())
a=list(map(int,input().split()))
h=[]
i=1
gap=1
while(gap<=n):
    h.append(gap)
    i+=1
    gap=(1<<i)-1
h.reverse()
for gap in h:
    for i in range(gap,n):
        temp=a[i]
        j=i
        while(j>=gap and a[j-gap]>temp):
            a[j]=a[j-gap]
            j-=gap
        a[j]=temp
    print(" ".join(map(str,a)))