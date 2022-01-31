use std::fs;
use std::path::Path;

fn parse_boj_file_name() {}

fn main() {
    let paths = fs::read_dir("../problems/boj").unwrap();

    for path in paths {
        println!("{}", path.unwrap().path().display());
    }
}
