from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        compl = {")" : "(", "}" : "{", "]" : "["}

        for i in s:
            if i in "({[":
                stack.append(i)
            else: 
                # check logic
                if len(stack) == 0 or stack[-1] != compl[i]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
        

        