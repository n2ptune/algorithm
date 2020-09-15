| Time Submmited   | Status   | Runtime | Memory  | Language   |
| ---------------- | -------- | ------- | ------- | ---------- |
| 09/13/2020 22:44 | Accepted | 76 ms   | 37.2 MB | javascript |

## 1480. Running Sum of 1d Array

원문: [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) `nums` 배열이 주어지고 `nums` 배열과 길이가 같은 배열을 반환해야한다. 그 배열의 i번째 원소는 nums의 i번째 원소의 값과 그 이전 값들을 더한 값이어야 한다. 아래는 예시로 주어진 입력과 출력 값이다.

```js
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

`[1, 2, 3, 4]`로 이루어진 배열을 입력받았으니 i가 0이라면 첫번째 원소는 `nums` 배열의 첫번째 원소 값이 그대로 오면 된다. i가 1이면 `nums` 배열의 인덱스가 0인 값과 1인 값을 더하여 3이 된다. 이런식으로 구성된 배열을 반환하면 된다.

여러가지 방법이 있겠지만 `nums` 배열을 순회하면서 현재 인덱스 이전의 값들을 모두 더해놓으면 문제를 훨씬 쉽게 풀 수 있다고 생각했다.

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  var temp = 0
  var result = []

  for (var i = 0; i < nums.length; i++) {
    temp += nums[i]
    result.push(temp)
  }

  return result
}
```

`temp` 변수에 배열의 값을 모두 더해놓는다. 그리고 매번 배열을 순회할 때마다 반환할 배열에 저장한다. 그리고 마지막에 배열을 반환하면 끝
