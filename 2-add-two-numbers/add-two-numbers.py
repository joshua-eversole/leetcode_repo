# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = 0
        power = 0
        # While both values have power, 
        while l1 and l2:
            value += (l1.val + l2.val) * 10**power
            power += 1
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value += l1.val * 10**power
            power += 1
            l1 = l1.next
        
        while l2:
            value += l2.val * 10**power
            power += 1
            l2 = l2.next

        digits = [int(d) for d in str(value)][::-1]
        dummy = ListNode()
        current = dummy
        for d in digits:
            current.next = ListNode(d)
            current = current.next
        return dummy.next
        

        


        