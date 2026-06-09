from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid) , len(grid[0])
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        
        queue = deque()
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 0:
                    current = 0
                    queue.append((i,j))
                
        while queue:
            r,c = queue.popleft()
            for (dr,dc) in directions:
                nr,nc = r+dr, c+dc
                if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]>0 and grid[nr][nc]>(grid[r][c]+1):
                    queue.append((nr,nc))
                    grid[nr][nc]=grid[r][c]+1
    

                        
                    
                   
    