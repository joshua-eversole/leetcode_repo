# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def popIn(merged, list_node):
            merged.next = list_node
            list_node = list_node.next
            merged = merged.next
            return merged, list_node
        pointer = ListNode(0)
        result = pointer
        while list1 and list2:
            if list1.val < list2.val:
                pointer, list1 = popIn(pointer, list1)
            else:
                pointer, list2 = popIn(pointer, list2)
        while list1:
                pointer, list1 = popIn(pointer, list1)
        while list2:
                pointer, list2 = popIn(pointer, list2)
        return result.next
            

        
                