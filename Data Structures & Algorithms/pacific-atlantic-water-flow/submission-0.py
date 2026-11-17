class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i,j,visit):
            if (i,j) in visit:
                return 
            
            visit.add((i,j))
            l,r,u,d = (i,j-1),(i,j+1),(i-1,j),(i+1,j)
            for nr,nc in [l,r,u,d]:
                if (
                    nr >= 0 and nr < ROWS
                    and nc >= 0 and nc < COLS
                    and heights[nr][nc] >= heights[i][j]
                ):
                    dfs(nr,nc,visit)

        for i in range(ROWS):
            dfs(i,0,pac)
            dfs(i,COLS-1,atl)
        for i in range(COLS):
            dfs(0,i,pac)
            dfs(ROWS-1,i,atl)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        return res


        