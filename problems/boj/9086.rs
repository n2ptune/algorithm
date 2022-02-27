use std::io;

fn main() {
  let mut count = String::new();

  io::stdin().read_line(&mut count);

  let n: i32 = count.trim().parse().unwrap();

  for i in 0..n {
    let mut ans = String::new();
    io::stdin().read_line(&mut ans);

    let first_char = ans.chars().next().unwrap();
    let last_char = ans.trim_end().chars().rev().next().unwrap();
    println!("{}{}", first_char, last_char);
  }
}