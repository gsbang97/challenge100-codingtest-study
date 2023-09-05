
def mergeTwoLists(self, l1, l2):
    start = temp = ListNode(0)

    while l1 and l2:
        if l1.val >= l2.val:
            temp.next = l2
            l2 = l2.next

        else:
            temp.next = l1
            l1 = l1.next

        temp = temp.next


    temp.next = l2 if not l1 else l1
    return start.next