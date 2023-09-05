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
        nodes = []
        curr = head

        if not curr:
            return curr
        if not curr.next:
            return curr
        while curr:
            nodes.append(curr)
            curr = curr.next

        re = nodes.pop()
        curr = re
        while nodes:
            curr.next = nodes.pop()
            curr = curr.next
        curr.next = None
        return re