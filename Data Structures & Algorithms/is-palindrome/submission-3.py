class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr=0
        rptr=len(s)-1
        

        while lptr<=rptr:
            if not s[lptr].isalnum():
                lptr += 1
                continue
            if not s[rptr].isalnum():
                rptr -= 1
                continue


            if s[lptr].lower() != s[rptr].lower():
                return False
            lptr +=1 
            rptr -=1 

        return True
        