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