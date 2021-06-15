"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None

        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1

        temp = head

        if n == 1:
            while (temp.next.next != None):
                temp = temp.next
            temp.next = None
            return head

        elif n == size:
            return head.next
        else:
            num = size - n

            for i in range(size - n - 1):
                temp = temp.next

            temp.next = temp.next.next
            return head

