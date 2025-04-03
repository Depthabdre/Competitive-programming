# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  

       
        mid = self.getMiddle(head)
        right_head = mid.next
        mid.next = None 

       
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)

       
        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head: ListNode) -> ListNode:
        """Finds the middle node using slow and fast pointers."""
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        """Merges two sorted linked lists."""
        dummy = ListNode()  
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next

        
        tail.next = left if left else right

        return dummy.next  
