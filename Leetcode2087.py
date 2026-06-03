from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res=0
        if(startPos[0]>homePos[0]):
            for i in range(homePos[0],startPos[0]):
                res+=rowCosts[i]
        elif(startPos[0]<homePos[0]):
            for i in range(startPos[0]+1,homePos[0]+1):
                res+=rowCosts[i]
        if(startPos[1]>homePos[1]):
            for i in range(homePos[1],startPos[1]):
                res+=colCosts[i]
        elif(startPos[1]<homePos[1]):
            for i in range(startPos[1]+1,homePos[1]+1):
                res+=colCosts[i]
        return res

print(Solution().minCost([1, 0], [2, 3], [5, 4,3], [8, 2, 6, 7]))