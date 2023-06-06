class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if char_map[word1[j]] > char_map[word2[j]]:
                        return False
                    break
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False

        return True    
