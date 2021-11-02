// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

struct Solution;

impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut vhead = Some(Box::new(ListNode { val: 0, next: head }));
        let mut slow = &mut vhead;
        let mut fast = &mut slow.clone();
        
        for _ in 0..=n {
            fast = &mut fast.as_mut().unwrap().next;
        }

        while fast.is_some() {
            slow = &mut slow.as_mut().unwrap().next;
            fast = &mut fast.as_mut().unwrap().next;
        }

        let next = &slow.as_mut().unwrap().next.as_mut().unwrap().next;
        slow.as_mut().unwrap().next = next.clone();

        return vhead.unwrap().next;
    }
}

fn main() {
    let node1 = Some(Box::new(ListNode { 
		val: 1,
		next: Some(Box::new(ListNode {
			val: 2,
			next: Some(Box::new(ListNode {
				val: 3,
				next: None,
			}))
		}))
    }));
    println!("{:?}", Solution::remove_nth_from_end(node1, 1));
    // println!("{:?}", (0..10).collect::<Vec<i32>>());
    // println!("{:?}", (1..=11).collect::<Vec<i32>>());
}