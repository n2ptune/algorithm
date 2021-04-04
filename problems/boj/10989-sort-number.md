## 수 정렬하기 3

[문제](https://www.acmicpc.net/problem/10989)의 시간 제한은 3초로 비교적 여유로운 편이며 메모리 제한은 8MB로 매우 여유롭지 않은 편이다.

입력되는 숫자를 모두 배열에 담아두고 입력이 끝나면 정렬하는 방법은 메모리가 초과되기 때문에 다른 방법을 사용해야 한다.

만 개의 배열을 미리 만들어 놓고 (0으로 초기화) 입력으로 들어오는 숫자의 인덱스를 카운팅한다. 모든 카운팅이 완료되면 0이 아닌 원소의 인덱스를 출력한다. (카운팅된 갯수만큼) 비효율적인 생각이지만 다른 좋은 방법이 떠오르지 않아서 이렇게 풀이를 작성했다...

```py
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
```
