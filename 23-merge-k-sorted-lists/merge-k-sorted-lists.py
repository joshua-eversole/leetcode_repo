# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                merged_list.append(self.mergeLists( l1, l2))
            lists = merged_list
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        point = dummy
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        while l1:
            point.next = l1
            l1 = l1.next
            point = point.next
        if l2:
            point.next = l2
            l2 = l2.next
            point = point.next
        return dummy.next

            