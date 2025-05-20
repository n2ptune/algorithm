N = int(input())
v = [[False]*N for _ in range(N)]
m = []
ans = 0
temp = 0
ansm = []
searching = False

for _ in range(N):
  m.append(list(map(int, list(input()))))


def search(x, y):
  if v[y][x]: return
  
  global searching
  global ans
  global temp

  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  v[y][x] = True

  if not m[y][x] == 0:
    if not searching:
      searching = True
      ans += 1
      temp += 1
    else:
      temp += 1
    for i in range(4):
      gx = dx[i] + x
      gy = dy[i] + y
      if gx >= 0 and gy >= 0 and N > gx and N > gy:
        search(gx, gy)
  

for i in range(N):
  for j in range(N):
    search(j, i)
    ansm.append(temp)
    temp = 0
    searching = False

print(ans)
print(*list(sorted(filter(lambda x: not x == 0, ansm))), sep='\n')