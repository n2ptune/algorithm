T = int(input())
ans = [0 for i in range(0, 2000002)]

for i in range(0, 1000001):
  c = sum(map(int, list(str(i))))
  if ans[i + c] == 0:
    ans[i + c]= i

print(ans[T])