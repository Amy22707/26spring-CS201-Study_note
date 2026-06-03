from typing import List
from collections import defaultdict,Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n=len(source)
        m=len(allowedSwaps)
        fa=[i for i in range(n)]
        size=[1]*n
        def find(x):
            if(fa[x]!=x):
                fa[x]=find(fa[x])
            return fa[x]
        def merge(x,y):
            fx=find(x)
            fy=find(y)
            if(fx==fy):
                return
            if(size[fx]<size[fy]):
                fx,fy=fy,fx
            fa[fy]=fx
            size[fx]+=size[fy]
        for i in range(m):
            merge(allowedSwaps[i][0],allowedSwaps[i][1])
        d=defaultdict(list)
        for i in range(n):
            d[find(i)].append(i)
        ans=0
        for lst in d.values():
            cnt=Counter(source[i] for i in lst)
            for i in lst:
                if(cnt[target[i]]>0):
                    cnt[target[i]]-=1
                else:
                    ans+=1
        return ans

print(Solution().minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]))