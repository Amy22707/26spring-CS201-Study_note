class Solution:
    def rotate(self,mat):
        n=len(mat)
        for i in range(1,n):
            for j in range(i):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for i in range(n):
            for j in range(n//2):
                mat[i][j],mat[i][n-j-1]=mat[i][n-j-1],mat[i][j]
        return mat
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for i in range(4):
            if(mat==target):
                return True
            self.rotate(mat)
        return False