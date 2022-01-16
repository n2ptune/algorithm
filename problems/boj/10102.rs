fn main() {
    let winner = {
        let mut input = String::new();
        std::io::stdin().read_line(&mut input);
        std::io::stdin().read_line(&mut input);

        let mut a = 0;
        let mut b = 0;

        for ch in input.trim().chars() {
            if ch == 'A' {
                a += 1;
            } else if ch == 'B' {
                b += 1;
            }
        }

        if a == b {
            "Tie"
        } else if a > b {
            "A"
        } else {
            "B"
        }
    };

    println!("{}", winner);
}
