n = int(input())
a, b = 0, 1
for _ in range(n):
  a, b = (a + b) % 1000000007, a % 1000000007
print(a)