# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def add(path, node):
            path.next = node
            path = path.next
            node = node.next
            return path, node
        
        result = ListNode(0)
        dummy = result

        while list1 and list2:
            if list1.val < list2.val:
                result, list1 = add(result, list1)
            else:
                result, list2 = add(result, list2)
        
        while list1:
            result, list1 = add(result, list1)
        
        while list2:
            result, list2 = add(result, list2)
        
        return dummy.next

