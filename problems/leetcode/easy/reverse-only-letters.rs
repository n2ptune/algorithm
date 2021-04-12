impl Solution {
  pub fn reverse_only_letters(s: String) -> String {
      let mut stack = Vec::new();
      for ch in s.chars() {
          let asc: u32 = ch as u32;
          if (asc >= 65 && asc <= 90) || (asc >= 97 && asc <= 122) {
              stack.push(ch);
          }
      }
      let mut ans = String::new();
      for ch in s.chars() {
          let asc: u32 = ch as u32;
          if (asc >= 65 && asc <= 90) || (asc >= 97 && asc <= 122) {
              ans.push_str(&stack.pop().unwrap().to_string());
          } else {
              ans.push_str(&ch.to_string());
          }
      }
      ans
  }
}