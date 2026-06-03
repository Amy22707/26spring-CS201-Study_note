from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        n=len(commands)
        m=len(obstacles)
        qwq=set(map(tuple,obstacles))
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        res=0
        x=0
        y=0
        dir=0
        for i in range(n):
            k=commands[i]
            if(k==-2):
                dir=(dir+3)%4
            elif(k==-1):
                dir=(dir+1)%4
            else:
                for j in range(k):
                    if((x+dx[dir],y+dy[dir]) in qwq):
                        break
                    x+=dx[dir]
                    y+=dy[dir]
            res=max(res,x*x+y*y)
        return res

print(Solution().robotSim([4,-1,3], []))