class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i,j):
            grid[i][j] = 'X'
            l, r, u, d = (i, j-1), (i, j+1), (i-1, j), (i+1, j)
            for dr, dc in [l,r,u,d]:
                if ( dr>=0
                    and dr<ROWS 
                    and dc>=0 
                    and dc<COLS 
                    and grid[dr][dc] == "1"
                ):
                    dfs(dr,dc)


        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
                    
        return count