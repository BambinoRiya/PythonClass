class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def helper(word,curr):
            found = False
            for i in range(len(word)):
                if word[i] == '.':
                    for char in curr.children:
                        found = found or helper(word[i+1::],curr.children[char])
                    return found
               
                if word[i] not in curr.children:
                    return False

                curr = curr.children[word[i]]
            return curr.is_end

        return helper(word,self.root)
            
  
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
