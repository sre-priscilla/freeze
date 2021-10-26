struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }
        let mut bitmap: [i32; 26] = [0; 26];
        let schars: Vec<char> = s.chars().collect();
        let tchars: Vec<char> = t.chars().collect();
        for i in 0..s.len() {
            let si: usize = schars[i] as usize - 97;
            let ti: usize = tchars[i] as usize - 97;
            bitmap[si] += 1;
            bitmap[ti] -= 1;
        }
        return bitmap.iter().all(|&x| x == 0);
    }
}

fn main() {
    println!("{}", Solution::is_anagram(String::from("anagram"), String::from("nagaram")));
    println!("{}", Solution::is_anagram(String::from("rat"), String::from("car")));
}