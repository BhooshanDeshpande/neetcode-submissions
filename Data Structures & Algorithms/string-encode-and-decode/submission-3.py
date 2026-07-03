'''
simplest solution limited to ASCII characters
'''

class Solution:

    def __init__(self):
        self.sep = "\u270B"

    def encode(self, strs: List[str]) -> str:
        append_str = ""
        for i in strs:
            append_str += i
            append_str += self.sep
        
        return append_str

    def decode(self, s: str) -> List[str]:
        return s.split(self.sep)[:-1]


