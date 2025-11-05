# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # The intuition is to take each number (and the carry if it exists), add it up, then put it in a new listnode
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        pointer = result
        while l1 or l2 or carry:
            # get the two values
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            # Calculate the digit to be added
            digit = n1 + n2 + carry
            if digit >= 10:
                carry = 1
                digit = digit % 10
            else:
                carry = 0
            # Add the digit, then move forward the linked lists
            pointer.next = ListNode(digit)
            pointer = pointer.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return result.next
            
            
        