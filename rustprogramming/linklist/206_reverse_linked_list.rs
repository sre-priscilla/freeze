// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
	pub val: i32,
	pub next: Option<Box<ListNode>>
}

impl ListNode {
	#[inline]
	#[warn(dead_code)]
	fn new(val: i32) -> Self {
		ListNode {
			next: None,
			val
		}
	}
}

struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
		let mut curr: Option<Box<ListNode>> = head;

		// while let Some(mut p) = curr.take() {
		// 	let next = p.next.take();
		// 	p.next = prev.take();
		// 	prev = Some(p);
		// 	curr = next;
		// }

		while !curr.is_none() {
			let next = curr.as_mut().unwrap().next.take();
			curr.as_mut().unwrap().next = prev;
			prev = curr;
			curr = next;
		}

      	return prev;
    }
}

fn main() {
	// let node1 = Some(Box::new(ListNode { 
	// 	val: 1,
	// 	next: Some(Box::new(ListNode {
	// 		val: 2,
	// 		next: Some(Box::new(ListNode {
	// 			val: 3,
	// 			next: None,
	// 		}))
	// 	}))
    // }));

	let mut node1 = Some(Box::new(ListNode::new(1)));
	node1.as_mut().unwrap().next = Some(Box::new(ListNode::new(2)));
	node1.as_mut().unwrap().next.as_mut().unwrap().next = Some(Box::new(ListNode::new(3)));
}