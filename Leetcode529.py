from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m=len(board)
        n=len(board[0])
        dx=[0,-1,-1,-1,0,1,1,1]
        dy=[-1,-1,0,1,1,1,0,-1]
        def dfs(x,y):
            if(board[x][y]=='X'):
                return
            elif(board[x][y]=='M'):
                board[x][y]='X'
                return
            elif(board[x][y]=='E'):
                cnt=0
                for i in range(8):
                    xx=x+dx[i]
                    yy=y+dy[i]
                    if(0<=xx<m and 0<=yy<n):
                        if(board[xx][yy]=='M'):
                            cnt+=1
                if(cnt>0):
                    board[x][y]=str(cnt)
                else:
                    board[x][y]="B"
                    for i in range(8):
                        xx=x+dx[i]
                        yy=y+dy[i]
                        if(0<=xx<m and 0<=yy<n):
                            dfs(xx,yy)
            return
        dfs(click[0],click[1])
        return board
print(Solution().updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],[3,0]))