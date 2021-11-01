use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, Vec<String>> = HashMap::with_capacity(strs.len());
        for str in strs.iter() {
            let mut counter: [u8; 26] = [0; 26];
            for ch in str.chars() {
                counter[ch as usize - 97] += 1;
            }
            let key: String = counter.iter()
                .map(|x| x.to_string())
                .collect::<Vec<String>>()
                .join("_");
            map.entry(key).or_insert(vec![]).push(str.clone());
        }
        return map.values().map(|v| (*v).clone()).collect();
    }
}

fn main() {
    let original_strs: Vec<&str> = vec!["eat", "tea", "tan", "ate", "nat", "bat"];
    let strs: Vec<String> = original_strs.iter().map(|s| String::from(*s)).collect();
    println!("{:?}", Solution::group_anagrams(strs));
}