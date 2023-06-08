# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head is not None and head.next is not None:
            first_node = head
            second_node = head.next

            # Swapping the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Updating the references
            prev = first_node
            head = first_node.next

        return dummy.next
