class Solution:
    def getArea(self, x, y, i, j) -> int:
      h = min([x, y])
      l = abs(i - j)

      return h * l

    def maxArea(self, height) -> int:
      ans = []
      l = 0
      r = len(height) - 1
      while r - l > 0:
        ans.append(self.getArea(height[l], height[r], l, r))
        if height[l] <= height[r]:
          l += 1
        else:
          r -= 1

      return max(ans)


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))