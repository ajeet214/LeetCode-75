class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = 'AEIOUaeiou'
        lst = [i for i, v in enumerate(s) if v in vowels]
        s = list(s)
        i = 0
        j = len(lst)-1
        while i < j:
            s[lst[i]], s[lst[j]] = s[lst[j]], s[lst[i]],
            i += 1
            j -= 1
        return ''.join(s)


obj = Solution()
print(obj.reverseVowels('leetcode'))

"""
Runtime: 45 ms
Memory: 18.7 MB
"""