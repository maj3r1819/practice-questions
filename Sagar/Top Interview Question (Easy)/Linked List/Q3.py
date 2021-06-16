"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

https://www.youtube.com/watch?v=XDO6I8jxHtA
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev