"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing
together the nodes of the first two lists.
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]


"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        curr = head1

        if head1 is None:
            head1 = head2

        else:
            while (curr.next is not None):
                curr = curr.next
            curr.next = head2

        curr = head1
        while (curr is not None):
            next = curr.next
            while (next is not None):
                if curr.val > next.val:
                    temp = curr.val
                    curr.val = next.val
                    next.val = temp
                next = next.next
            curr = curr.next

        return head1


