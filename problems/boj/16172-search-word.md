## 나는 친구가 적다 (Large)

solved.ac 서비스에서 매겨진 티어는 골드 4인데 실제 난이도는 그렇지 않은 문제이다. 문자열 두 개가 주어지는데 두 번째로 주어진 문자열이 첫 번째로 주어진 문자열에 속해있으면 1을 출력하고 그렇지 않으면 0을 출력하는 문제이다. 다만 첫 번째로 주어진 문자열에 따로 처리를 해주어야 한다.

입력은 모두 알파벳 소문자와 대문자로만 주어지지만 첫 번째 문자열에는 숫자가 포함되어 있을 수도 있다. 그렇기에 숫자를 지워주는 작업을 한 뒤 두 번째 문자열이 포함되어 있는지만 체크하면 풀리는 간단한 문제이다.

```python
import sys
read = sys.stdin.readline


def toAlpha(x):
  if (ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x) <= 122):
    return True
  else:
    return False


S = filter(toAlpha, list(read().rstrip()))
K = read().rstrip()
L = ''.join(list(S))

print(1 if not L.find(K) == -1 else 0)
```
