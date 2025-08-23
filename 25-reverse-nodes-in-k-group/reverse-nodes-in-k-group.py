class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        # Ensure we can flip everything in this
        def longEnough(node):
            for _ in range(k):
                if not node:
                    return False
                node = node.next
            return True

        # Go through and flip every value, and return the beginning and end of the flip
        def flip(first_node):
            prev = None
            curr = first_node
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            first_node.next = curr
            return prev, first_node 
        

        # Loop through the logic until we get too close to the end to flip a new section
        while longEnough(group_prev.next):
            start = group_prev.next
            new_head, new_tail = flip(start)
            group_prev.next = new_head
            group_prev = new_tail

        return dummy.next
