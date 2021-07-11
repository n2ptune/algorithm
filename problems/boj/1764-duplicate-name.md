## 듣보잡

[문제](https://www.acmicpc.net/problem/1764)는 프로그래머스에서 풀었던 마라톤 경주 문제와 비슷한데, 듣도 못한 사람의 리스트와 보도 못한 사람의 리스트가 주어지고 각각의 리스트에 공통적으로 들어가 있는 사람을 구하는 문제이다.

받는 사람들의 이름을 `dict`의 키 형태로 저장시킨 다음 듣도 보도 못한 사람의 수는 두 리스트 길이 중 짧은 리스트의 길이보다 클 수 없기 때문에 더 작은 쪽의 키 값을 큰 쪽의 `dict`에서 찾는다. 모두 찾고 이름을 정렬한다음 리스트의 갯수와 함꼐 출력한다.

```py
import sys
read = sys.stdin.readline

N, M = map(int, read().split(' '))
A = {}
B = {}

for _ in range(N):
  A[read().rstrip()] = 1

for _ in range(M):
  B[read().rstrip()] = 1

ans = []

if N >= M:
  for k in B.keys():
    if A.get(k):
      ans.append(k)
else:
  for k in A.keys():
    if B.get(k):
      ans.append(k)

ans.sort()

print(len(ans))
print('\n'.join(ans))
```
