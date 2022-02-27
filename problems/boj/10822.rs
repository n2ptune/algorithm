use std::io;

fn main() {
  let mut st = String::new();

  io::stdin().read_line(&mut st);

  let v: Vec<i32> = st.trim_end().split(',').map(|s| s.parse().unwrap()).collect();
  let sum: i32 = v.iter().sum();
  println!("{}", sum);
}