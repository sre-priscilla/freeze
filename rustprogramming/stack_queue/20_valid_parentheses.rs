struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = vec![];
        for ch in s.chars() {
            if stack.is_empty() {
                stack.push(ch);
            } else {
                let last = *stack.last().unwrap();
                match (last, ch) {
                    ('(', ')') | ('[', ']') | ('{', '}') => {stack.pop();},
                    _ => stack.push(ch),
                };
            }
        }
        return stack.is_empty();
    }
}

fn main() {
    println!("{}", Solution::is_valid(String::from("()")));
    println!("{}", Solution::is_valid(String::from("()[]{}")));
    println!("{}", Solution::is_valid(String::from("(]")));
    println!("{}", Solution::is_valid(String::from("([)]")));
    println!("{}", Solution::is_valid(String::from("{[]}"))); 
}