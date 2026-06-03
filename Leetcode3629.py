from collections import deque,defaultdict
from typing import List
from math import sqrt
MX=1000001
factors=[[] for _ in range(MX)]
for i in range(2,MX):
    if(not factors[i]):
        for j in range(i,MX,i):
            factors[j].append(i)
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n=len(nums)
        m=max(nums)
        groups=defaultdict(list)
        for i in range(n):
            for p in factors[nums[i]]:
                groups[p].append(i)
        q=deque()
        q.append((0,0))
        vis=[0]*n
        vis[0]=1
        while(q):
            idx,steps=q.popleft()
            if(idx==n-1):
                return steps
            cur=groups[nums[idx]]
            cur.append(idx+1)
            if(idx-1>=0):
                cur.append(idx-1)
            for i in cur:
                if(i!=idx and not vis[i]):
                    vis[i]=1
                    q.append((i,steps+1))
            cur.clear()
print(Solution().minJumps([1,2,4,6]))