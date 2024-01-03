use std::io;

fn main() {
    solve_11382();
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