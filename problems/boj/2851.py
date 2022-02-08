import sys

read = sys.stdin.readline

nums = [int(read()) for _ in range(10)]
ans = 0
flag = False

for i in range(len(nums) - 1):
  ans += nums[i]
  if ans + nums[i + 1] >= 100:
    flag = True
    p = (ans + nums[i + 1]) - 100
    m = 100 - ans

    if p > m:
      print(ans)
    elif m > p or m == p:
      print(ans + nums[i + 1])
    break

if not flag:
  print(sum(nums))