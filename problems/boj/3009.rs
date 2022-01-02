use std::io;

fn main() {
  let mut x: Vec<i32> = Vec::new();
  let mut y: Vec<i32> = Vec::new();

  for _ in 0..3 {
    let mut s = String::new();
    io::stdin().read_line(&mut s);
    
    let z = s.trim().split(' ').collect::<Vec<&str>>();

    x.push(z[0].parse::<i32>().unwrap());
    y.push(z[1].parse::<i32>().unwrap());
  }

  let mut ansx: i32 = 0;
  let mut ansy: i32 = 0;

  for i in 0..3 {
    let x_count = x.iter().filter(|&n| *n == x[i]).count();
    let y_count = y.iter().filter(|&n| *n == y[i]).count();

    if x_count == 1 {
       ansx = x[i];
    }

    if y_count == 1 {
      ansy = y[i];
    }
  }

  println!("{} {}", ansx, ansy);
}