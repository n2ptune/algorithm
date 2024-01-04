fn solve_25314() {
  let mut input = String::new();
  io::stdin().read_line(&mut input).expect("");
  let n: i32 = input.trim().parse::<i32>().unwrap();
  let r: i32 = n / 4;
  let result: String = String::from("long ").repeat(r as usize);
  println!("{} int", result.trim());
}