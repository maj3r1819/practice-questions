"""
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mylist = []
        curr = head
        while curr is not None:
            mylist.append(curr.val)
            curr = curr.next

        mid = len(mylist) // 2
        count = 0
        for i in range(mid):
            if mylist[i] == mylist.pop():
                count += 1

        if count == mid:
            return True

        else:
            return False
