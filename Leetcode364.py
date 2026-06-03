class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        m=len(grid)
        n=len(grid[0])
        i=x
        j=x+k-1
        while(i<j):
            grid[i][y:y+k],grid[j][y:y+k]=grid[j][y:y+k],grid[i][y:y+k]
            i+=1
            j-=1
        return grid
print(Solution().reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],1,0,3))