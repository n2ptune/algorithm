n = int(input())
a, b = 0, 1
n = n % (15 * 100000)
for i in range(n):
  a, b = b % 1000000, (a + b) % 1000000
print(a)