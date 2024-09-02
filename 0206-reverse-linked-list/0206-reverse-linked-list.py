# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        previous = None
        current = head
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current 
            current = next_node
        
        return previous
                       