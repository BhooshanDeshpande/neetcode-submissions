class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = [0]*26

        for char in s:
            char_freq[ord(char) - ord('a')] +=  1
        
        for char in t:
            char_freq[ord(char) - ord('a')] -=  1

        if set(char_freq) == {0}:
            return True
        
        return False
        