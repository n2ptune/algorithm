fn main() {
    let nums: (i32, i32) = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let d: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();

        (d[0], d[1])
    };

    let mut v: Vec<i32> = Vec::new();
    let mut i = 1;

    loop {
        if v.len() >= nums.1 as usize {
            break;
        }

        for _ in 0..i {
            v.push(i);
        }

        i += 1;
    }

    let vb: i32 = v[(nums.0 - 1) as usize..nums.1 as usize].iter().sum();
    println!("{}", vb);
}
