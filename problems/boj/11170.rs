fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let count: i32 = input.trim().parse::<i32>().unwrap();

    for _ in 0..count {
        let nums: (i32, i32) = {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            let v: Vec<i32> = s
                .split_whitespace()
                .map(|s| s.parse::<i32>().unwrap())
                .collect();

            (v[0], v[1])
        };

        let mut count = 0;

        for i in nums.0..(nums.1 + 1) {
            let v: String = i.to_string();
            let rm = v.replace("0", "");

            if v.len() != rm.len() {
                count += v.len() - rm.len();
            }
        }

        println!("{}", count);
    }
}
