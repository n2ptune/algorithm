use std::io;

fn main() {
    solve_25314();
}

fn solve_11382() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");

    let numbers: Vec<u128> = input
        .split_whitespace()
        .map(|s| s.parse::<u128>())
        .filter_map(Result::ok)
        .collect();
    let sum: u128 = numbers.iter().sum();

    println!("{}", sum);
}

fn solve_25314() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");
    let n: i32 = input.trim().parse::<i32>().unwrap();
    let r: i32 = n / 4;
    let result: String = String::from("long ").repeat(r as usize);
    println!("{} int", result.trim());
}