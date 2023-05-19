class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        word1_len = len(word1)
        word2_len = len(word2)

        if word1_len < word2_len:
            min_len = word1_len
            p = word2
        elif word1_len == word2_len:
            min_len = word1_len
            p = ''
        else:
            min_len = word2_len
            p = word1

        s = ''
        for i in range(min_len):
            s += word1[i] + word2[i]

        return s + p[min_len:]

