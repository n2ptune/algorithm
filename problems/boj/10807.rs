fn main() {
    let ans: i32 = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s);

        let _n: i32 = s.trim().parse().unwrap();

        s = String::new();
        std::io::stdin().read_line(&mut s);

        let vm: Vec<i32> = s
            .split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();

        s = String::new();
        std::io::stdin().read_line(&mut s);

        let v: i32 = s.trim().parse().unwrap();
        let vb: Vec<i32> = vm.into_iter().filter(|s| s == &v).collect();

        vb.len() as i32
    };

    println!("{}", ans);
}
