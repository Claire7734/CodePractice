# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        carry = 0
        ret = ListNode() #dummyHead
        sum = ret
        while (l1 != None) and (l2 != None):
            sum.next = ListNode()
            sum = sum.next
            cur_sum = l1.val + l2.val + carry
            if cur_sum >= 10:
                cur_sum -= 10
                carry = 1
            else:
                carry = 0
            sum.val = cur_sum
            l1 = l1.next
            l2 = l2.next
        
        if l1 == None:
            l = l2
        else:
            l = l1
        
        while l != None:
            sum.next = ListNode()
            sum = sum.next
            cur_sum = l.val + carry
            if cur_sum >= 10:
                cur_sum -= 10
                carry = 1
            else:
                carry = 0
            sum.val = cur_sum
            l = l.next
        
        if carry != 0:
            sum.next = ListNode(carry)
        
        return ret.next # TODO: delete head
        
