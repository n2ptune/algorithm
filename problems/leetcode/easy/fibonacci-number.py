class Solution:
  def fib(self, n: int) -> int:
    f = [0, 1, 1]
    if n <= 2:
      return f[n]
    else:
      for i in range(n - 2):
        f.append(f[-1] + f[-2])
      return f[-1]
