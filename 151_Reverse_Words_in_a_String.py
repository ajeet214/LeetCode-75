class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


obj = Solution()
print(obj.reverseWords('this is python'))

"""
Runtime: 39 ms
Memory: 16.5 MB
"""