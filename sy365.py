def heapify(heap,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and heap[l]>heap[largest]):
        largest=l
    if(r<n and heap[r]>heap[largest]):
        largest=r
    if(largest!=i):
        heap[i],heap[largest]=heap[largest],heap[i]
        heapify(heap,n,largest)
n=int(input())
heap=list(map(int,input().split()))
for i in range(n//2-1,-1,-1):
    heapify(heap,n,i)
print(*heap)