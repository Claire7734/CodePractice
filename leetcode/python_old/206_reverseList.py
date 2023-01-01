# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1: # Iteration
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2: # Recursion
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None #MARK!!!!
        return ret            
