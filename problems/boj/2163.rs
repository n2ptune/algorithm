fn main() {
  let (a, b): (i32, i32) = {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    let v = buf.trim().split(' ').map(|x| x.parse().unwrap()).collect::<Vec<i32>>();
    (v[0], v[1])
  };
  
  println!("{}", a * b - 1);
}