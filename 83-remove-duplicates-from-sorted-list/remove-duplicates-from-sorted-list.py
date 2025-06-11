# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Thought of the optimal solution to this pretty quickly, not too much extra thought involved here. Was a little unsure on the best way to skip the duplicate list, 
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        kept_val = head.val
        node = head
        while node:
            nxt = node.next

            # If we have, delete (use a while loop for long lists of the same val)
            while nxt and nxt.val == node.val:
                nxt = nxt.next
            # If we've reached the end, adjust node and nxt for the next run of the while loop
            node.next = nxt
            node = nxt
        
        return head

