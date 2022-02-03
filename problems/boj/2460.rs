fn main() {
    let ans: i32 = {
        let mut person = 0;
        let mut n: Vec<i32> = Vec::new();
        for _ in 0..10 {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s);
            let v: Vec<i32> = s
                .trim()
                .split_whitespace()
                .map(|s| s.parse::<i32>().unwrap())
                .collect();
            person -= v[0];
            person += v[1];
            n.push(person);
        }
        *(n.iter().max().unwrap())
    };
    println!("{}", ans);
}
