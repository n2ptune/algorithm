## 전화번호 목록

주어진 전화번호 목록이 일관성이 있는지를 테스트한다. 한 번호가 다른 번호의 접두어가 된다면 일관성이 없다고 판단한다. 예를 들어 123456789 라는 전화번호가 있고 123으로 시작하는 전화번호가 있다면 이 전화번호 목록은 일관성이 없다고 판단한다.

전화번호 목록을 글자 수대로 정렬하고 반복해서 비교한다.

```py
import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
  q = []
  N = int(read())
  for __ in range(N):
    q.append(read().rstrip())
  q.sort()
  flag = True
  for i in range(len(q) - 1):
    if q[i] == q[i+1][0:len(q[i])]:
      flag = False
      break
  print('YES' if flag else 'NO')
```
