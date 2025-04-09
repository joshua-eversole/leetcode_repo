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
        # Assign the value from node.next to node, erasing the original node's value
        node.val = node.next.val

        # Make the next node the second node (skip the node that repeats the value)
        node.next = node.next.next
        