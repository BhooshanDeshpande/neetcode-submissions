class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs = ["act","pots","tops","cat","stop","hat"]

        sort_strs = ["act", "opts", .....]

        dict_anagrams = [act: (0,3), opts: (1,2,4), ...]
        '''
        def strsort(string):
            return "".join(sorted(string))

        sort_strs = {}
        for i in range(len(strs)):
            if not strsort(strs[i]) in sort_strs: 
                sort_strs[strsort(strs[i])] = [i]
            else:
                sort_strs[strsort(strs[i])].append(i) 

        return_lst = []
        for _, v in sort_strs.items():
            group_ana = []
            for idx in v:
                group_ana.append(strs[idx])
            return_lst.append(group_ana)

        return return_lst

        
        


        



        

        

        