class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end= False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.add(word)

        curr = trie.root
        res = ''
        while curr:
            if len(curr.children)>1 or curr.is_end:
                return res

            key = list(curr.children)[0]
            res +=key
            curr = curr.children[key]

        return res
        
