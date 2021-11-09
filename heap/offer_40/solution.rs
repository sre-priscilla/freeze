struct Solution;

impl Solution {
    fn heapify(arr: &mut Vec<i32>) {
        for i in (0..arr.len() / 2).rev() {
            Solution::sift_down(arr, i)
        }
    }

    fn heappop(arr: &mut Vec<i32>) -> i32 {
        let last = arr.len() - 1;
        arr.swap(0, last);
        let ret = arr.pop().unwrap();
        if arr.len() > 1 {
            Solution::sift_down(arr, 0)
        }
        return ret;
    }

    // fn sift_up(arr: &mut Vec<i32>, i: usize) {
    //     let mut p = i;
    //     while p > 0 && arr[p] < arr[(p - 1) / 2] {
    //         arr.swap(p, (p - 1) / 2);
    //         p = (p - 1) / 2;
    //     } 
    // }

    fn sift_down(arr: &mut Vec<i32>, i: usize) {
        let mut p = i;
        while p < arr.len() / 2 {
            let mut _min = p;
            if 2 * p + 1 < arr.len() && arr[2 * p + 1] < arr[_min] {
                _min = 2 * p + 1;
            }
            if 2 * p + 2 < arr.len() && arr[2 * p + 2] < arr[_min] {
                _min = 2 * p + 2;
            }
            if p == _min {
                break;
            }
            arr.swap(p, _min);
            p = _min;
        }
    }

    pub fn get_least_numbers(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let mut nums = arr.clone();
        Solution::heapify(&mut nums);
        
        let mut ret = vec![];
        for _ in 0..k {
            ret.push(Solution::heappop(&mut nums));
        }
        return ret;
    }
}

fn main() {
    println!("{:?}", Solution::get_least_numbers(vec![1, 2, 3, 4, 5], 2));
}