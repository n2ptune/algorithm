class Solution:
    def intToRoman(self, num: int) -> str:
      i = 0
      ans = ''
      r = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
      ]

      while len(r) > i:
        a, b = r[i]

        if num >= a:
          num = num - a
          ans += b

        if a > num: i += 1

      return ans

print(Solution().intToRoman(20))