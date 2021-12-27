use std::io;

fn main() {
  let mut arr: Vec<i32> = Vec::new();
  let mut iter_str: String = String::new();

  io::stdin().read_line(&mut iter_str).ok().expect("error");

  let iter_count: i32 = iter_str.trim().parse().unwrap();

  for _ in 0..iter_count {
    let mut s = String::new();
    io::stdin().read_line(&mut s);
    arr.push(s.trim().parse().unwrap());
  }

  arr.sort();

  for i in &arr {
    println!("{}", i);
  }
}