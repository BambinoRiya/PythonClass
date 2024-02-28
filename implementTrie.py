class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.children[ord(char)-97] is None:
                curr.children[ord(char)-97] = TrieNode()
            curr = curr.children[ord(char)-97]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not(curr.children[ord(char)-97]):
                return False
            curr = curr.children[ord(char)-97]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not(curr.children[ord(char)-97]):
                return False
            curr = curr.children[ord(char)-97]
        return True

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
