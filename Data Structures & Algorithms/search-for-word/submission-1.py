class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        h, w = len(board), len(board[0])
        def isValid(r,c):
            if 0 <= r and r < h and 0 <= c and c < w:
                return True
            return False

        def dfs(start: Tuple, index: int):           
            if index == len(word):
                return True
            
            i, j = start[0], start[1]
            temp = board[i][j]
            board[i][j] = "#"
            l, r, u, d = (i, j-1), (i, j+1), (i-1, j), (i+1, j)
            ans = False
            for nr, nc in [l, r, u, d]:
                if isValid(nr, nc) and board[nr][nc] == word[index]:
                    print("Pass", board[nr][nc], nr, nc)
                    ans = ans or dfs((nr,nc), index+1)
                
            board[i][j] = temp    
            return ans

        starts = set()
        for i in range(0, h):
            for j in range(0, w):
                if board[i][j] == word[0]:
                    starts.add((i, j))

        if len(starts) == 0:
            return False
        
        for start in starts: 
            if dfs(start, 1):
                return True
            print("Fail", start)
        return False
