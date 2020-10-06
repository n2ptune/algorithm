| Time Submmited   | Status   | Runtime | Memory  | Language   |
| ---------------- | -------- | ------- | ------- | ---------- |
| 10/06/2020 04:14 | Accepted | 96 ms   | 43.2 MB | javascript |

## 605. Can Place Flowers

원문: [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

문제 내용은 그다지 어려운 부분이 없다. `flowerbed` 라는 화단이 주어지고 화단에는 꽃이 심어져 있는 부분과 꽃이 심어져 있지 않은 부분이 주어진다. 심어져 있는 부분은 1, 그렇지 않은 부분은 0으로 채워진다.

심어져 있는 부분의 양 옆은 꽃을 심을 수 없는 규칙이 있으며 두 번째 입력으로는 심어야할 꽃의 갯수가 주어진다. 이 갯수 이상 만큼 꽃을 심을 수 있다면 `true`를 반환하고, 주어진 갯수 만큼 꽃을 심을 수 없다면 `false`를 반환하면 되는 문제이다.

```js
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let count = 0

  for (let i = 0; i < flowerbed.length; i++) {
    if (
      flowerbed[i - 1] !== 1 &&
      flowerbed[i + 1] !== 1 &&
      flowerbed[i] !== 1
    ) {
      flowerbed[i] = 1
      count++
    }
  }

  return count >= n
}
```

배열의 요소를 순회하면서, 양 옆이 1이 아니라면 추가할 수 있는 갯수를 하나 늘리고 계속 순회한다. 그리고 갯수가 `n`보다 크면 `true`를 반환하고 그렇지 않으면 `false`를 반환한다.

문제는 주어진 `n`개의 꽃을 심을 수 있는지만 물어보기 때문에, `count`를 늘려가면서 `n`을 넘어가면 바로 `true`를 반환하면 런타임 시간을 좀 더 줄일 수 있다.

```js
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let count = 0

  for (let i = 0; i < flowerbed.length; i++) {
    if (
      flowerbed[i - 1] !== 1 &&
      flowerbed[i + 1] !== 1 &&
      flowerbed[i] !== 1
    ) {
      flowerbed[i] = 1
      count++

      if (count >= n) {
        return true
      }
    }
  }

  return count >= n
}
```

런타임 시간이 **96ms**에서 **80ms**까지 줄고 메모리 값도 조금 줄었다.
