| Time Submmited   | Status   | Runtime | Memory  | Language   |
| ---------------- | -------- | ------- | ------- | ---------- |
| 09/09/2020 14:52 | Accepted | 208 ms  | 46.9 MB | javascript |

## 9. Palindrome Number

원문: [Palindrome Number](https://leetcode.com/problems/palindrome-number/) 정수를 뒤집었을 때, 뒤집지 않은 오리지널 정수와 같으면 그 정수를 **palindrome number**라고 한다. 이 문제에서는 음의 정수 혹은 양의 정수를 입력받고 그 수를 뒤집어 본래 수와 비교하면 쉽게 풀어낼 수 있다.

먼저, 음의 정수로 받는 모든 경우는 **palindrome number**가 될 수 없다. 이유는 음의 정수는 앞에 마이너스(-) 기호가 반드시 붙기 때문에 이 기호와 함께 수를 뒤집으면 절대 본래 수와 똑같아질 수가 없다. 그러므로 0보다 작은 수가 입력으로 들어올 시 **palindrome number**가 아니다.

자바스크립트에서는 표준 내장 함수로 문제를 아주 쉽게 풀 수 있다. 먼저 입력받은 정수를 문자열로 변환시키고 그 문자열을 배열로 잘라 뒤집는다. 그리고 배열의 원소를 모두 합친다.

키워드는 `split`, `reverse`, `join`이다. 이 세가지를 활용해서 문제를 풀었다.

```js
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false

  var s = x.toString()
  var r = s.split('').reverse().join('')

  return s === r
}
```
