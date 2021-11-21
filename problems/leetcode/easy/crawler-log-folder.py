class Solution:
  def minOperations(self, logs: list[str]) -> int:
    ans = 0
    for log in logs:
      if log == './':
        continue
      if ans == 0 and log == '../':
        continue
      ans += 1 if log != '../' else -1
    return ans
