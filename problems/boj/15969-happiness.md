## 행복

[문제](https://www.acmicpc.net/problem/15969)에서는 학생의 수와 학생들의 점수가 입력으로 오고 제일 점수가 큰 학생의 점수와 제일 작은 학생의 점수의 차이를 출력하면 되는 문제다. 입력으로 오는 최대 갯수는 1000개이므로 언어에서 제공하는 정렬을 사용해도 크게 문제가 없을 것 같은데, 파이썬에서는 `min`과 `max`로 배열의 최대, 최솟값을 쉽게 구할 수 있다.

```py
import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().rstrip().split(' ')))

print(max(nums) - min(nums))
```