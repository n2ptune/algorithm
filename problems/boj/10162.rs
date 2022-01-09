fn main() {
  let mut t: i32 = {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    
    s.trim().parse().unwrap()
  };
  
  let a = 300;
  let b = 60;
  let c = 10;
  
  let af = t / a;
  t = t % a;
  let bf = t / b;
  t = t % b;
  let cf = t / c;
  t = t % c;

  if t > 0 {
    println!("-1");
  } else {
    println!("{} {} {}", af, bf, cf);
  }
}