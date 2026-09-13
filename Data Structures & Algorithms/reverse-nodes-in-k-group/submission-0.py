# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev = None
            curr = head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1

        if count == k:
            reversed_head = reverse(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head

        return head
    

        