# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        # First thoughts: have two node pointers at any given time, and 
        placeholder = ListNode(0)
        placeholder.next = head
        runner = head
        list_len = 0
        while runner and n > 0:
            runner = runner.next
            n -= 1

        
        pointer = placeholder
        while runner:
            runner = runner.next
            pointer = pointer.next
        
        if pointer and pointer.next:
            pointer.next = pointer.next.next
        
        return placeholder.next
        

        