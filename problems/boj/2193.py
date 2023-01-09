# no filter -> 1, 2, 4, 8, 16, 32, ....
# filter -> f(n) = arr[n - 2] + arr[n - 1]
d = [1, 1, 2, 3]
n = int(input())

if n <= len(d):
  print(d[n - 1])
else:
  while len(d) < 90:
    d.append(d[-2] + d[-1])
  print(d[n - 1])
