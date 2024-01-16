class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        if len(set(s)) == len(s):
          return len(s)

        su = ''
        for ch in s:
          if ch not in su:
            su += ch
            ans = max(ans, len(su))
          else:
            su = su.split(ch)[1] + ch

        return ans

print(Solution().lengthOfLongestSubstring('babc'))