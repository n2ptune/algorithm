class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == ''.join(list(reversed(list(s))))
    def longestPalindrome(self, s: str) -> str:
        p = ''

        for i in range(0, len(s) + 1):
            for j in range(i+1, len(s) + 1):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > len(p):
                    p = s[i:j]

        return p

print(Solution().longestPalindrome('cbbd'))