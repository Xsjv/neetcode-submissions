class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        a = len(word1)
        b = len(word2)
        while a > 0 and b > 0:
            final += word1[len(word1) - a]
            final += word2[len(word2) - b]
            a -= 1
            b -= 1
        if a == 0:
            final += word2[len(word2) - b:]
        else:
            final += word1[len(word1) - a:]
        return final
        