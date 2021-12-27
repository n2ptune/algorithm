use std::io;
use std::collections::{BinaryHeap};

fn main() {
  let mut heap = BinaryHeap::<i32>::new();
  let mut s = String::new();

  io::stdin().read_line(&mut s).ok().expect("error");

  let count: i32 = s.trim().parse().unwrap();

  for _ in 0..count {
    let mut a = String::new();
    io::stdin().read_line(&mut a).ok().expect("error");
    heap.push(a.trim().parse().unwrap());
  }

  let a = heap.into_vec();

  for _ in 0..heap.len() {
    println!("{:?}", a);
  }
}