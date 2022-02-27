import sys
read = sys.stdin.readline

N = int(read())
nums = [0 for _ in range(10000)]

for _ in range(N):
  nums[int(read()) - 1] += 1

for i in range(10000):
  if not nums[i] == 0:
    for j in range(nums[i]):
      print(i + 1)
