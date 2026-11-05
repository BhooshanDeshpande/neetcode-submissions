class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Brute force :
            go thru each str : (o(n))
                go thru each char : o(m) 
                    create map
            compare maps and group strings in the same order

        '''
        dct = {}
        for s in strs:  
            key_match = False          
            for key in dct.keys():
                if sorted(s) == sorted(key):
                    key_match = True
                    dct[key].append(s)
                    break
            
            if not key_match: 
                dct[s] = []
            

        res = []
        for k, v in dct.items():
            v.append(k)
            res.append(v)

        return res