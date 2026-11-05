class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        l = t = 0
        r = b = n-1

        while l < r and t < b : 
            for i in range(0, r - l):
                tmp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tmp
            l += 1
            t += 1
            r -= 1
            b -= 1
        
        