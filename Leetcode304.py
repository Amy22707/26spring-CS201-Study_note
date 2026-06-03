class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        m=len(matrix)
        n=len(matrix[0])
        sum=[[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                sum[i+1][j+1]=sum[i+1][j]+sum[i][j+1]+matrix[i][j]-sum[i][j]
        self.sum=sum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj=NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))