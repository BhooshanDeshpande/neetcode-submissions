class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        start l at first, r at last
        compare until l > r
            if alphanum, move that ptr 
            if lowercase equal, move both 
            else return false
        """

        l, r = 0, len(s)-1
        while l <= r:
            if r < 0 or l > len(s)-1: 
                print("Pointer left the chat")
                return False

            if not s[l].isalnum():
                print("found {} moving l".format(s[l])) 
                l +=1 
                continue
            
            if not s[r].isalnum():
                print("found {} moving r".format(s[r])) 
                r -=1
                continue

            print("Compare  {} - {}".format(s[l], s[r]))
            if  s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True 
        