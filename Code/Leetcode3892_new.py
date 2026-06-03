import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if(n//2<k):
            return -1
        a=[0]*n
        for i in range(n):
            p=nums[i-1]
            q=nums[i]
            r=nums[(i+1)%n]           
            a[i]=max(0,max(p,r)+1-q)
        l=[0]*n
        r=[0]*n
        for i in range(n):
            l[i]=(i-1+n)%n
            r[i]=(i+1)%n
        q=[]
        heapq.heapify(q)
        for i in range(n):
            heapq.heappush(q,(a[i],i))
        vis=[0]*n
        ans=0
        cnt=0
        while(cnt<k):
            if(not q):
                return -1
            val,idx=heapq.heappop(q)
            if(vis[idx]):
                continue
            ans+=val
            vis[l[idx]]=1
            vis[r[idx]]=1
            a[idx]=a[l[idx]]+a[r[idx]]-val
            heapq.heappush(q,(a[idx],idx))
            l[idx]=l[l[idx]]
            r[idx]=r[r[idx]]
            l[r[idx]]=idx
            r[l[idx]]=idx
            cnt+=1
        return ans
print(Solution().minOperations([2,1,2],1))
