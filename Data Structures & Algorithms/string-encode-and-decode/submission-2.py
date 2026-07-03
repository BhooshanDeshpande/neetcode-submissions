class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += f"{len(i)}#"
            encoded_str += i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        num_letters = ""
        words = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                num_letters += s[i]
                i += 1
                continue
            
            # now i is '#'
            end = i + int(num_letters) 
            num_letters = "" # reset
            word = ""
            i += 1 # skipping '#'
            while i <= end:
                word += s[i]
                i += 1
            
            words.append(word)

        return words
            






