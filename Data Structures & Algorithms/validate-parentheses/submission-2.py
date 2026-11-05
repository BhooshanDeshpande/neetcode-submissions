class Solution:
    def isValid(self, s: str) -> bool:
        brac_match = { ")" : "(" , "}" : "{" , "]" : "[" }
        stack = []

        for item in s:
            if item in ["(", "{", "["]:
                stack.append(item)
        
            if item in [")", "}", "]"]:
                if len(stack) == 0:
                     return False
                     
                if brac_match[item] != stack[-1]: 
                    return False
                stack.pop()
        
        if stack == []:
            return True
        return False