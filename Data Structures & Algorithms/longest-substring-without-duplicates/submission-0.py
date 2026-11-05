class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute force:
            start with first, note max substr len until char repeats
            iterate for all 
            return max substr len found so far
            o(n2)

        sliding window:
            start l and r at first, keep a map of letters
            count max len, until a repeat char appears
            move the l, r to after repeat character, flush map
            iterate until r is reached end
            return max len

        Tricky: 
        "zxyabyz" 0-->6
        """

        if len(s) in (0, 1):
            return len(s)

        l, r, max_len = 0, 1, 1
        dct = {s[l] : True}
        while (r <= len(s) - 1):
            if dct.get(s[r]) == None:
                # r is not there in the dct
                lght = r - l + 1 
                dct.update({s[r] : True})
                if lght > max_len:
                    max_len = lght
            else:
                while (s[l] != s[r]):
                    l += 1 
                l += 1
                r = l       
                dct.clear()
                dct.update({s[l] : True})
            
            r += 1

        return max_len



