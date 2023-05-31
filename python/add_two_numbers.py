#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #add numbers on the same node index. 
            #if there are no more remaining nodes on both, end. 
            #if there are nodes remaining on at least one thread, keep going 
                #but skip the add if and keep going to then ext one.
        
        ### chapt gpt's optimized solution 
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        #simple solution
        res = ListNode(0)
        current = res
        h1 = l1
        h2 = l2

        while h1 or h2:
            if h1 and h2:
                total = h1.val + h2.val + current.val
                if total >= 10:
                    current.val = total - 10
                    current.next = ListNode(1)
                else:
                    current.val = total
                    if h1.next or h2.next:
                        current.next = ListNode(0)
                h1 = h1.next
                h2 = h2.next
                current = current.next
            elif h1 and not h2:
                total = h1.val + current.val
                if total >= 10:
                    current.val = total - 10
                    current.next = ListNode(1)
                else:
                    current.val = total
                    if h1.next:
                        current.next = ListNode(0)
                h1 = h1.next
                current = current.next
            elif h2 and not h1:
                total = h2.val + current.val
                if total >= 10:
                    current.val = total - 10
                    current.next = ListNode(1)
                else:
                    current.val = total
                    if h2.next:
                        current.next = ListNode(0)
                h2 = h2.next
                current = current.next

        return res
