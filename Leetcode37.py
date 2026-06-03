class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        row=[0]*9
        col=[0]*9
        block=[[0 for _ in range(3)]for _ in range(3)]
        spaces=[]
        def flip(i,j,digit):
            row[i]^=(1<<digit)
            col[j]^=(1<<digit)
            block[i//3][j//3]^=(1<<digit)
        def dfs(step):
            global valid
            if(step==len(spaces)):
                return True
            i,j=spaces[step]
            mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
            while(mask):
                qaq=mask&(-mask)
                digit=bin(qaq).count('0')-1
                flip(i,j,digit)
                board[i][j]=str(digit+1)
                if(dfs(step+1)):
                    return True
                flip(i,j,digit)
                board[i][j]='.'
                mask&=(mask-1)
            return False

        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    flip(i,j,int(board[i][j])-1)
        while(True):
            flag=False
            for i in range(9):
                for j in range(9):
                    if(board[i][j]=='.'):
                        mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
                        if(not (mask&(mask-1))):
                            digit=bin(mask).count('0')-1
                            flip(i,j,digit)
                            board[i][j]=str(digit+1)
                            flag=True
            if(not flag):
                break
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    spaces.append((i,j))
        dfs(0)
        """
        Do not return anything, modify board in-place instead.
        """
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
for i in range(9):
    for j in range(9):
        print(board[i][j],end=" ")
    print()