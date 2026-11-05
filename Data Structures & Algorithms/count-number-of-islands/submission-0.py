class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def dfs(r,c):
            visited.add((r,c))
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            for d in dirs: 
                dr, dc = d[0], d[1]
                rnew, cnew = r + dr, c + dc 
                if rnew in range(rows) \
                    and cnew in range(cols) \
                    and grid[rnew][cnew] == "1" \
                    and (rnew, cnew) not in visited:
                        dfs(rnew,cnew)
                     
        for r in range(rows):
            for c in range(cols):
                ele = grid[r][c]
                if ele == "1" and (r,c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands

        
        