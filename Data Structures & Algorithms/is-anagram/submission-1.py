class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
        verbal explanation
        seen = { 
            r = 0
            c = 0
            a = 0
            e = 0

        
        }


        '''

        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1
            
            if t[i] not in seen:
                seen[t[i]] = -1
            else:
                seen[t[i]] -= 1

        for k,v in seen.items():
            if  v != 0: 
                return False
        
        return True
        
        
        