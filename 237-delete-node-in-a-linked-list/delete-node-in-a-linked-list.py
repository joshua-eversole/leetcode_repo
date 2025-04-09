# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Shift the value to the end
        while node.next.next:
            node.val = node.next.val
            node = node.next
        
        #now that we're at the end, do it one more time but make node.next = None
        node.val = node.next.val
        node.next = None

        