class Trie:
    def __init__(self):
        self.eow = False
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for i, p in enumerate(word):
            if p not in curr.children:
                trie = Trie()
                curr.children[p] = trie
            curr = curr.children[p]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, p in enumerate(word):
            if p not in curr.children.keys():
                return False
            curr = curr.children[p]
        return curr.eow
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, p in enumerate(prefix):
            if p not in curr.children.keys():
                return False
            curr = curr.children[p]
        return True

        
        