## 1550. Three Consecutive Odds

연속적으로 홀수가 3번 나오는지 안나오는지를 반환한다. 카운터 변수를 하나 만들고 짝수를 만날 때마다 0으로 초기화한다. 반대로 홀수를 만나면 1씩 증가시키고 3을 넘으면 `true`를 반환한다.

```rs
impl Solution {
  pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
      let mut count: i32 = 0;
      for num in arr.iter() {
          if num % 2 == 0 {
              count = 0;
          } else {
              count += 1;
              if count >= 3 {
                  return true
              }
          }
      }
      return false
  }
}
```
