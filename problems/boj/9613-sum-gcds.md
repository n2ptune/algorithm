## GCD 합

> [문제 원문](https://www.acmicpc.net/problem/9613)

정수 리스트에서 두 수를 선택해서 얻을 수 있는 최대공약수를 모두 더해서 반환하는 문제, 최대공약수를 구하는 문제는 [유클리드 호제법을 이용한 방법](https://www.imkh.dev/algorithm-gcd-lcm/)으로 쉽게 구할 수 있다. 그 외에 생각할 건 두 수의 조합인데, 한 수를 선택해서 얻을 수 있는 모든 조합은 두 수의 위치가 바뀐다고 해도(a, b 꼴에서 b, a 꼴로) 최대 공약수는 바뀔 일이 없으니 두 수의 순서는 상관없다. 그러므로 현재 인덱스의 정수와 현재 인덱스 앞에 정수들에 대한 모든 최대 공약수를 구해서 리스트에 담아둔다.

이 과정을 반복한 뒤 모든 최대 공약수들의 합을 구해서 반환한다.

```py
import sys
read = sys.stdin.readline


def gcd(a, b):
  r = 0
  while not b == 0:
    r = a % b
    a = b
    b = r
  return a


for i in range(int(read())):
  n = list(map(int, read().split(' ')))[1:]
  gcds = []
  for k, t in enumerate(n):
    if len(n) - 1 <= k:
      break
    for m in n[k + 1:]:
      gcds.append(gcd(t, m))
  print(sum(gcds))
```
